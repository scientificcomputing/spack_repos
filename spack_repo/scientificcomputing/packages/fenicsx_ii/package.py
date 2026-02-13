# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class FenicsxIi(PythonPackage):
    """FEniCSx_ii is an extension of FEniCSx that allows users to work with non-conforming 3D-1D meshes.
    The core algorithm is based on the framework proposed by Kuchta 2021 and implemented in FEniCS_ii.
    """

    homepage = "https://scientificcomputing.github.io/fenicsx_ii/"
    url = "https://github.com/scientificcomputing/fenicsx_ii/archive/refs/tags/v0.4.0.tar.gz"
    git = "https://github.com/scientificcomputing/fenicsx_ii.git"

    maintainers("jorgensd")

    license("MIT", checked_by="jorgensd")

    version("main", branch="main")
    version("0.4.0", sha256="e3ec634ccb34e70c77f39bd3f7498910139f57653a09ef4278461f34bd72d9d1")
    
    variant("petsc", default=True, description="PETSc support")

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-setuptools@42:", type="build")

    depends_on("py-fenics-dolfinx@0.10:", when="@0.4:", type="run")
    depends_on("py-fenics-dolfinx@main", when="@main", type="run")
    depends_on("py-numpy", type="run")
    depends_on("py-packaging", type="run")

    with when("+petsc"):
        depends_on("py-petsc4py", type="run")
        depends_on("py-fenics-dolfinx+petsc4py", type="run")
