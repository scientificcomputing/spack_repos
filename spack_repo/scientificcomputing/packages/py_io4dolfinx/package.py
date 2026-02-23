# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyIo4dolfinx(PythonPackage):
    """io4dolfinx is an extension for py-fenics-dolfinx that provides advanced input/output capabilities.
    It focuses on N-to-M checkpointing (writing data on N processors, reading on M processors)
    and supports reading/writing various mesh formats using interchangeable backends.
    """

    homepage = "https://scientificcomputing.github.io/io4dolfinx/"
    url = "https://github.com/scientificcomputing/io4dolfinx/archive/refs/tags/v1.1.0.tar.gz"
    git = "https://github.com/scientificcomputing/io4dolfinx.git"

    maintainers("finsberg", "jorgensd")

    license("MIT", checked_by="jorgensd")

    version("main", branch="main")
    version("1.1.0", sha256="3641d72083858d5ae0672a16cb11dc6fd792a117cbc2281be307ffc47a91fcb2")

    variant("adios2", default=True, description="ADIOS2 backend support")
    variant("h5py", default=True, description="H5Py backend support")
    variant("xdmf", default=True, description="XDMF backend support")
    variant("vtkhdf", default=True, description="VTKHDF backend support")
    variant("pyvista", default=True, description="Pyvista backend support")

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("cxx", type="build")

    depends_on("py-fenics-dolfinx@0.9:", when="@1.1:", type="run")
    depends_on("py-fenics-dolfinx@main", when="@main", type="run")
    depends_on("py-numpy", type="run")
    depends_on("py-packaging", type="run")
    depends_on("py-setuptools@42:", type="build")

    with when("+adios2"):
        depends_on("adios2+python+hdf5", type=("build", "run"))

    with when("+h5py"):
        depends_on("py-h5py+mpi", type="run")

    with when("+vtkhdf"):
        depends_on("py-h5py+mpi", type="run")

    with when("+xdmf"):
        depends_on("py-h5py+mpi", type="run")

    with when("+pyvista"):
        depends_on("py-pyvista", type="run")
