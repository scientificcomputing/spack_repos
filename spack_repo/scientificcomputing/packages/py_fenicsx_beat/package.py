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

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-setuptools@42:", type="build")

    depends_on("py-fenics-dolfinx@0.10:+petsc4py", when="@0.2:", type="run")
    depends_on("py-fenics-dolfinx@main+petsc4py", when="@main", type="run")
    depends_on("py-fenics-basix", type="run")
    depends_on("py-fenics-ufl", type="run")
    depends_on("py-mpi4py", type="run")
    depends_on("py-scifem", type="run")
    depends_on("petsc+mumps", type="run")
    depends_on("py-numpy", type="run")
    depends_on("py-packaging", type="run")
    depends_on("py-rich", type="run")
    depends_on("py-pint", type="run")
    depends_on("py-scipy", type="run")
