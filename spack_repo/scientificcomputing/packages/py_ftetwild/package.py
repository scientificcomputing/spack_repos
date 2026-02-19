# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFtetwild(PythonPackage):
    """Python interface to tetrahedralize using ftetwild
    """

    homepage = "https://github.com/pyvista/pytetwild"
    url = "https://github.com/pyvista/pytetwild/archive/refs/tags/v0.2.3.tar.gz"
    git = "https://github.com/jorgensd/pytetwild"
    #"https://github.com/pyvista/pytetwild.git"

    maintainers("jorgensd")

    license("MPL", checked_by="jorgensd")

    version("main", branch="dokken/find-nanobind", submodules=True)
    #version("0.2.3", sha256="4f6e9d86cccac4f6028a4796d7ea2b4bbe3a86b9d89b4348a2f1cb5307a4054e")
    
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-nanobind@1.3.2:", when="@0.2.3:", type="build")
    depends_on("py-scikit-build-core@0.10: +pyproject", when="@0.2.3:", type="build")
    depends_on("gmp", type="build")
    
    depends_on("py-numpy", type="run")
