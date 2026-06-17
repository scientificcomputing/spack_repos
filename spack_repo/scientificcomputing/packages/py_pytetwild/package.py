# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytetwild(PythonPackage):
    """Python interface to tetrahedralize using ftetwild"""

    homepage = "https://github.com/pyvista/pytetwild"
    url = "https://github.com/pyvista/pytetwild/archive/refs/tags/v0.2.3.tar.gz"
    git = "https://github.com/pyvista/pytetwild"

    maintainers("jorgensd")

    license("MPL", checked_by="jorgensd")

    version("main", branch="main", submodules=True)
    version("0.2.3", tag="v0.2.3", submodules=True)
    version("0.3.0", tag="v0.3.0", submodules=True)

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-nanobind@1.3.2:", when="@0.2.3:", type="build")
    depends_on("py-scikit-build-core@0.10: +pyproject", when="@0.2.3:", type="build")
    depends_on("gmp", type="build")

    depends_on("py-numpy", type="run")

    def patch(self):
        if self.spec.satisfies("@0.2.3"):
            # Get nanobind cmake path through python
            patch_nanobind = """
            execute_process(
                COMMAND "${Python_EXECUTABLE}" -c "import nanobind; print(nanobind.cmake_dir())"
                OUTPUT_STRIP_TRAILING_WHITESPACE
                OUTPUT_VARIABLE NB_DIR
            )
            list(APPEND CMAKE_PREFIX_PATH "${NB_DIR}")

            """
            filter_file(
                r"find_package\(nanobind CONFIG REQUIRED\)",
                f"{patch_nanobind}find_package(nanobind CONFIG REQUIRED)",
                "CMakeLists.txt",
            )
