# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNetworksFenicsx(PythonPackage):
    """Solving PDEs on 1D branching networks in FEniCSx"""

    homepage = "https://scientificcomputing.github.io/networks_fenicsx/"
    url = "https://github.com/scientificcomputing/networks_fenicsx/archive/refs/tags/v0.2.0.tar.gz"
    git = "https://github.com/scientificcomputing/networks_fenicsx.git"

    maintainers("jorgensd")

    license("MIT", checked_by="jorgensd")

    version("main", branch="main")
    version("0.2.0", sha256="ddc680b73723eb54f18d6119343071381f5f73cac7ebe01fe50e205a59afe2f3")

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-setuptools@42:", type="build")

    depends_on("py-fenics-dolfinx@0.10:+petsc4py", when="@0.2:", type="run")
    depends_on("py-fenics-dolfinx@main+petsc4py", when="@main", type="run")
    depends_on("py-fenics-basix", type="run")
    depends_on("py-fenics-ufl", type="run")
    depends_on("py-mpi4py", type="run")
    depends_on("py-networkx", type="run")
    depends_on("petsc+mumps", type="run")
    depends_on("py-numpy", type="run")
    depends_on("py-packaging", type="run")
