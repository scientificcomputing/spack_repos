# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyWildmeshing(PythonPackage):
    """Python interface to triangulate and tetrahedralize using ftetwild or triwild"""

    homepage = "https://wildmeshing.github.io/python/"
    url = "https://github.com/wildmeshing/wildmeshing-python/archive/refs/tags/0.4.tar.gz"
    git = "https://github.com/wildmeshing/wildmeshing-python.git"

    maintainers("jorgensd")

    license("MPL", checked_by="jorgensd")

    version("main", branch="main", submodules=True)
    version("0.4", commit="bc835076c1e2b2c92fe5364f5bc7f4119e6c5fd3", submodules=True)

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-numpy", type="run")
    depends_on("py-setuptools@42:", type="build")
    depends_on("py-svgwrite", type="run")
    depends_on("gmp", type="build")

    def patch(self):
        # 1. Disable the project's strict warnings module (often enables -Werror)
        filter_file(r"include\(Warnings\)", "#include(Warnings)", "CMakeLists.txt")

        # 2. Add global permissive flags immediately after project definition
        # -fpermissive: Fixes TBB "changes meaning" error
        # -Wno-error: Prevents warnings from stopping the build
        filter_file(
            r"project\(WildMeshing\)",
            "project(WildMeshing)\nadd_compile_options(-fpermissive -Wno-error -Wno-array-bounds -Wno-stringop-overflow)",
            "CMakeLists.txt",
        )

        # 3. Patch the WindingNumber.h header immediately after download.
        # We inject a 'sed' command into CMakeLists.txt to insert pragma ignores
        # at the top of the header file. This guarantees the warning is suppressed
        # regardless of target flags.

        # NOTE: The location of windingnumber.h is in a weird place
        patch_header_cmd = (
            "execute_process(COMMAND sed -i "
            r'"1i #pragma GCC diagnostic ignored \"-Warray-bounds\"\n#pragma GCC diagnostic ignored \"-Wstringop-overflow\"" '
            "${THIRD_PARTY_DIR}tetwild/src/external/WindingNumber.h)"
        )

        filter_file(
            r"wildmeshing_download_tetwild\(\)",
            f"wildmeshing_download_tetwild()\n{patch_header_cmd}",
            "CMakeLists.txt",
        )

        # 4. Patch svgpathtools for "modern" python

        filter_file(
            "from collections import MutableSequence",
            "from collections.abc import MutableSequence",
            join_path("wildmeshing", "parse_svg", "svgpathtools", "path.py"),
        )
