import hashlib
import json
import os
import re
import urllib.request
from pathlib import Path

# Token is provided by GitHub Actions to avoid rate limits
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")


def get_github_latest_release(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/tags"
    req = urllib.request.Request(url)
    if GITHUB_TOKEN:
        req.add_header("Authorization", f"Bearer {GITHUB_TOKEN}")
    try:
        with urllib.request.urlopen(req) as response:
            tags = json.loads(response.read().decode())
            if not tags:
                return None, None

            # Filter for tags that look like semver (e.g., v1.0.0, 0.9.4)
            valid_tags = [t["name"] for t in tags if re.match(r"^v?\d+\.\d+", t["name"])]
            if not valid_tags:
                return None, None

            # Sort to find the highest semver release
            def parse_version(tag):
                return [int(x) for x in re.findall(r"\d+", tag)]

            latest_tag = max(valid_tags, key=parse_version)

            # Spack versions typically drop the leading 'v'
            spack_ver = latest_tag[1:] if latest_tag.startswith("v") else latest_tag
            return spack_ver, latest_tag
    except Exception as e:
        print(f"Failed to fetch from GitHub for {owner}/{repo}: {e}")
        return None, None


def get_pypi_latest_release(pypi_string):
    # pypi_string example: "annotated-doc/annotated_doc-0.0.4.tar.gz"
    pkg_name = pypi_string.split("/")[0]
    url = f"https://pypi.org/pypi/{pkg_name}/json"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            latest_version = data["info"]["version"]

            # Find sdist sha256 checksum
            for release in data["releases"].get(latest_version, []):
                if release["packagetype"] == "sdist":
                    return latest_version, release["digests"]["sha256"]
            return latest_version, None
    except Exception as e:
        print(f"Failed to fetch from PyPI for {pkg_name}: {e}")
        return None, None


def compute_sha256(url):
    try:
        req = urllib.request.Request(url)
        if "api.github.com" in url and GITHUB_TOKEN:
            req.add_header("Authorization", f"Bearer {GITHUB_TOKEN}")
        with urllib.request.urlopen(req) as response:
            return hashlib.sha256(response.read()).hexdigest()
    except Exception as e:
        print(f"Failed to download and hash {url}: {e}")
        return None


def process_package(package_py_path):
    with open(package_py_path, "r") as f:
        content = f.read()

    new_version = None
    sha256 = None

    # Determine if package sources from PyPI or GitHub
    pypi_match = re.search(r'pypi\s*=\s*["\']([^"\']+)["\']', content)
    github_match = re.search(
        r'(?:git|url)\s*=\s*["\']https://github\.com/([^/]+)/([^/]+?)(?:\.git|/archive.*)["\']',
        content,
    )

    if pypi_match:
        new_version, sha256 = get_pypi_latest_release(pypi_match.group(1))
    elif github_match:
        owner, repo = github_match.groups()
        new_version, tag_name = get_github_latest_release(owner, repo)
        if new_version:
            # Check if this version is already declared
            if f'version("{new_version}"' in content or f"version('{new_version}'" in content:
                return False

            # Get sha256 for the new tarball
            tar_url = f"https://github.com/{owner}/{repo}/archive/refs/tags/{tag_name}.tar.gz"
            sha256 = compute_sha256(tar_url)

    if not new_version or not sha256:
        return False

    if f'version("{new_version}"' in content or f"version('{new_version}'" in content:
        return False

    print(f"Found new version {new_version} for {package_py_path.parent.name}")

    # Inject the new version block right after the last version() block
    lines = content.split("\n")
    last_version_idx = -1
    for i, line in enumerate(lines):
        if line.strip().startswith("version("):
            last_version_idx = i

    if last_version_idx != -1:
        new_line = f'    version("{new_version}", sha256="{sha256}")'
        lines.insert(last_version_idx + 1, new_line)

        with open(package_py_path, "w") as f:
            f.write("\n".join(lines))

        # Update CI matrix JSON so the new version gets tested automatically
        ci_config_path = Path(".github/ci-test-config.json")
        if ci_config_path.exists():
            with open(ci_config_path, "r") as f:
                ci_config = json.load(f)

            # Spack packages use underscores (py_scifem) but in CI specs they use dashes (py-scifem)
            spack_pkg_name = package_py_path.parent.name.replace("_", "-")

            if spack_pkg_name in ci_config:
                if new_version not in ci_config[spack_pkg_name]["versions"]:
                    # Insert right after 'main' if it exists, otherwise at start
                    if "main" in ci_config[spack_pkg_name]["versions"]:
                        ci_config[spack_pkg_name]["versions"].insert(1, new_version)
                    else:
                        ci_config[spack_pkg_name]["versions"].insert(0, new_version)

                    with open(ci_config_path, "w") as f:
                        json.dump(ci_config, f, indent=2)
                    print(f"Added {new_version} to CI matrix for {spack_pkg_name}")

        return True

    return False


if __name__ == "__main__":
    repo_dir = Path("spack_repo/scientificcomputing/packages")
    updates = 0
    for pkg_dir in repo_dir.iterdir():
        if pkg_dir.is_dir():
            pkg_file = pkg_dir / "package.py"
            if pkg_file.exists():
                if process_package(pkg_file):
                    updates += 1

    if updates > 0:
        print(f"Successfully updated {updates} packages.")
    else:
        print("All packages are up to date.")
