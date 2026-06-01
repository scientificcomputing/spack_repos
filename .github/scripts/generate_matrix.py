import json
import os


def generate_matrix():
    with open(".github/ci-test-config.json", "r") as f:
        config = json.load(f)

    matrix_include = []
    for pkg_name, details in config.items():
        for version in details["versions"]:
            for spec in details["specs"]:
                # Import name defaults to the package name without 'py-' if not provided
                import_name = details.get(
                    "import_name", pkg_name.replace("py-", "").replace("-", "_")
                )
                matrix_include.append(
                    {
                        "package": pkg_name,
                        "version": version,
                        "spec": spec,
                        "import_name": import_name,
                        "remote_repos": details.get("remote_repos", ""),
                    }
                )

    # Write the output to GitHub Actions environment
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"matrix={json.dumps(matrix_include)}\n")
    else:
        print(json.dumps(matrix_include, indent=2))


if __name__ == "__main__":
    generate_matrix()
