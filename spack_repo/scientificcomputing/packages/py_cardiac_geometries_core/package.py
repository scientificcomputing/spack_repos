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
#     spack install py-cardiac-geometries-core
#
# You can edit this file again by typing:
#
#     spack edit py-cardiac-geometries-core
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCardiacGeometriesCore(PythonPackage):
    """General ODE translator"""

    homepage = "https://computationalphysiology.github.io/cardiac-geometries-core"
    git = "https://github.com/ComputationalPhysiology/cardiac-geometries-core.git"
    url = "https://github.com/ComputationalPhysiology/cardiac-geometries-core/archive/refs/tags/v1.2.2.tar.gz"

    # notify when the package is updated.
    maintainers("finsberg")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("MIT", checked_by="finsberg")

    version("main", branch="main")
    version("1.2.2", sha256="bb7a003474d2f2013dcb2190ca1d30527f1e7aee3626114083f0656dc3830b9d")

    # Python version and Build backend
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@61.2:", type="build")

    # Core dependencies
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-gmsh@:4.13.1", type=("build", "run"))
    depends_on("gmsh@:4.13.1 ~fltk", type=("build", "run"))
    depends_on("py-rich-click", type=("build", "run"))
