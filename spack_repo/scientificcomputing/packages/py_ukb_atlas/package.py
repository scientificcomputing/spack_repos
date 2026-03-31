# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-ukb-atlas
#
# You can edit this file again by typing:
#
#     spack edit py-ukb-atlas
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyUkbAtlas(PythonPackage):
    """Biventricular atlas of the heart based on the UK Biobank dataset."""

    homepage = "https://computationalphysiology.github.io/ukb-atlas"
    git = "https://github.com/ComputationalPhysiology/ukb-atlas.git"
    url = "https://github.com/ComputationalPhysiology/ukb-atlas/archive/refs/tags/v0.12.0.tar.gz"

    # notify when the package is updated.
    maintainers("finsberg")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("MIT", checked_by="finsberg")

    version("main", branch="main")
    version("1.2.3", sha256="65bed1747a9e47f59300d39336af2282bb6fe5a6dc6dd7a7038dd6ba06af7333")

    # Python version and Build backend
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@61.2:", type="build")

    # Core dependencies
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-meshio@2.3.5:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-h5py+mpi", type=("build", "run"))
    depends_on("py-pyvista", type=("build", "run"))
    depends_on("py-gmsh@:4.13.1", type=("build", "run"))
    depends_on("gmsh@:4.13.1", type=("build", "run"))
    # OpenGL dependency for gmsh
    depends_on("mesa-glu", type=("build", "run"))
    # X11 library
    depends_on("libxcursor", type=("build", "run"))
    depends_on("libxft", type=("build", "run"))
    depends_on("libxrender", type=("build", "run"))
    depends_on("libxinerama", type=("build", "run"))
