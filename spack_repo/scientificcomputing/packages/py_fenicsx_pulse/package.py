# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFenicsxPulse(PythonPackage):
    """Library to run cardiac mechanics simulations in FEniCSx"""

    homepage = "https://finsberg.github.io/fenicsx-pulse/"
    url = "https://github.com/finsberg/fenicsx-pulse/archive/refs/tags/v0.6.0.tar.gz"
    git = "https://github.com/finsberg/fenicsx-pulse.git"

    maintainers("finsberg")

    license("MIT", checked_by="finsberg")

    version("main", branch="main")
    version("0.6.0", sha256="fddfb2fa554e6537b8205a1a7806549fbbd5b55cb913338387f54f27bef87818")

    variant(
        "cardiac-geometries", default=True, description="Add cardiac geometries as a dependency"
    )

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-setuptools@42:", type="build")

    depends_on("py-fenics-dolfinx +petsc4py", type=("build", "run"))
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
    depends_on("py-rich-argparse", type=("build", "run"))

    with when("+cardiac-geometries"):
        depends_on("py-cardiac-geometriesx", type=("build", "run"))
