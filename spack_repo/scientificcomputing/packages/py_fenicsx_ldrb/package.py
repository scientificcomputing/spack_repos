# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFenicsxLdrb(PythonPackage):
    """Library to run cardiac EP simulations in FEniCSx"""

    homepage = "https://finsberg.github.io/fenicsx-ldrb/"
    url = "https://github.com/finsberg/fenicsx-ldrb/archive/refs/tags/v0.1.17.tar.gz"
    git = "https://github.com/finsberg/fenicsx-ldrb.git"

    maintainers("finsberg")

    license("MIT", checked_by="finsberg")

    version("main", branch="main")
    version("0.1.17", sha256="19ce4660b9711d2efb2f9109d0bc6380eb9f2359a43f8f85f4207ee63f79f30c")

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-setuptools@42:", type="build")

    depends_on("py-io4dolfinx+adios2+xdmf", type=("build", "run"), when="@0.2:,main")
    depends_on("py-adios4dolfinx", type=("build", "run"), when="@:0.1")

    depends_on("py-fenics-dolfinx+petsc4py", type=("build", "run"))
    depends_on("py-fenics-basix", type=("build", "run"))
    depends_on("py-fenics-ufl", type=("build", "run"))
    depends_on("py-mpi4py", type=("build", "run"))
    depends_on("petsc+mumps", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
