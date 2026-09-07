# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDolfinxAdjoint(PythonPackage):
    """Automatic differentiation compatible with DOLFINx, built on
    pyadjoint's tape-based algorithmic differentiation.
    """

    homepage = "https://scientificcomputing.github.io/dolfinx-adjoint/"
    url = "https://github.com/scientificcomputing/dolfinx-adjoint/archive/refs/tags/v0.3.0.tar.gz"
    git = "https://github.com/scientificcomputing/dolfinx-adjoint.git"

    maintainers("finsberg", "jorgensd")

    license("MIT", checked_by="jorgensd")

    version("main", branch="main")
    version("0.3.0", sha256="aa9b2564a4e607be97c276a8986a23e4ea349f85dc8ffa28dfb33624d706f865")

    variant("scifem", default=False, description="Enable scifem support")
    variant("fenicsx-ii", default=False, description="Enable fenicsx_ii support")
    variant("moola", default=False, description="Enable moola optimisation backend support")

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-fenics-dolfinx@0.10:", when="@0.3:", type=("build", "run"))
    depends_on("py-fenics-dolfinx@main", when="@main", type=("build", "run"))
    depends_on("py-pyadjoint@2025.10:", when="@0.3:", type=("build", "run"))
    depends_on("py-pyadjoint@main", when="@main", type=("build", "run"))
    depends_on("py-packaging@24.2:", type=("build", "run"))
    depends_on("py-typing-extensions", when="^python@:3.10", type=("build", "run"))
    depends_on("py-setuptools@42:", type="build")

    with when("+scifem"):
        depends_on("py-scifem", type=("build", "run"))

    with when("+fenicsx-ii"):
        depends_on("py-fenicsx-ii", type=("build", "run"))

    with when("+moola"):
        depends_on("py-moola@0.1.6:", type=("build", "run"))
