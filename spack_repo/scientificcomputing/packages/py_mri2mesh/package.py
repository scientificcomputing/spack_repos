# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMri2mesh(PythonPackage):
    """Tool for converting labeled MRI data to a mesh."""

    homepage = "https://www.scientificcomputing.github.io/mri2mesh/"
    url = "https://github.com/scientificcomputing/mri2mesh/archive/v0.2.1.tar.gz"
    git = "https://github.com/scientificcomputing/mri2mesh.git"

    maintainers("finsberg")

    license("MIT", checked_by="jorgensd")

    version("main", branch="main")
    version("0.2.1", sha256="4aae1d4555b134d0827e9feaad685647cbc52cde2ae2eaf12a231e687603c09a")

    variant("mesh", default=True, description="Support meshing")

    depends_on("python@3.10:", when="@main:", type=("build", "run"))
    depends_on("py-packaging")
   
    depends_on("py-pyvista", type="run")
    depends_on("py-numpy", type="run")
    depends_on("py-matplotlib", type="run")
    depends_on("py-nibabel", type="run")
    depends_on("py-scikit-image", type="run")
    depends_on("py-scipy", type="run")
    depends_on("py-meshio@2.3.5:", type="run")
    
    depends_on("py-setuptools@42:", type="build")

    with when("+mesh"):
        depends_on("py-wildmeshing", type="run")
        depends_on("py-h5py+mpi", type="run")