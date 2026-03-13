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
    version("0.3.0", sha256="8b8091dc92264d3fcda3c23a897d9b65a50befc6a294dd4a157ec3a06734f4b4")

    variant("mesh", default=True, description="Support meshing")

    depends_on("python@3.10:", when="@main:", type=("build", "run"))
    depends_on("py-setuptools@42:", type="build")

    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-pyvista", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-nibabel", type=("build", "run"))
    depends_on("py-scikit-image", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-meshio@2.3.5:", type=("build", "run"))

    with when("+mesh"):
        depends_on("py-pytetwild", type=("build", "run"))
        depends_on("py-h5py+mpi", type=("build", "run"))
