# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFenicsxBeat(PythonPackage):
    """Library to run cardiac EP simulations in FEniCSx"""

    homepage = "https://finsberg.github.io/fenicsx-beat/"
    url = "https://github.com/finsberg/fenicsx-beat/archive/refs/tags/v0.2.3.tar.gz"
    git = "https://github.com/finsberg/fenicsx-beat.git"

    maintainers("finsberg")

    license("MIT", checked_by="finsberg")

    version("main", branch="main")
    version("0.2.4", sha256="ddba1ee2a4ded52a846b1ee11b1bd6e7d97522608dd6206436ae0fd58b12b17b")
    version("0.3.0", sha256="4dd8fefa122f86705945a6e2e5969dbf2a0fe987072b2a27f1298547717222a6")

    variant(
        "cardiac-geometries", default=True, description="Add cardiac geometries as a dependency"
    )

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-setuptools@42:", type="build")

    depends_on("py-fenics-dolfinx+petsc4py", type=("build", "run"))
    depends_on("py-fenics-basix", type=("build", "run"))
    depends_on("py-fenics-ufl", type=("build", "run"))
    depends_on("py-mpi4py", type=("build", "run"))
    depends_on("py-scifem", type=("build", "run"))
    depends_on("petsc+mumps", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-rich", type=("build", "run"))
    depends_on("py-pint", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))

    with when("+cardiac-geometries"):
        depends_on("py-cardiac-geometriesx", type=("build", "run"))
