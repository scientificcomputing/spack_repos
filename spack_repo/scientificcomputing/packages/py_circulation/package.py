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
#     spack install py-gotranx
#
# You can edit this file again by typing:
#
#     spack edit py-gotranx
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCirculation(PythonPackage):
    """General ODE translator"""

    homepage = "https://computationalPhysiology.github.io/gotranx"
    git = "https://github.com/ComputationalPhysiology/gotranx.git"
    url = "https://github.com/ComputationalPhysiology/gotranx/archive/refs/tags/v1.5.1.tar.gz"

    # notify when the package is updated.
    maintainers("finsberg")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("MIT", checked_by="finsberg")

    version("main", branch="main")
    version("1.2.1", sha256="7198386d06d0ebd00ec275c82592700eb2f5b2f1f5e1564e0b1c3baad8ddd934")

    # Python version and Build backend
    depends_on("python@3.11:", type=("build", "run"))
    depends_on("py-setuptools@61.2:", type="build")

    # Core dependencies
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pint", type=("build", "run"))
    depends_on("py-rich", type=("build", "run"))
