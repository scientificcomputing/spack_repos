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


class PyMyokit(PythonPackage):
    """tool for modeling and simulation of cardiac cellular electrophysiology"""

    homepage = "https://github.com/myokit/myokit"

    url = "https://github.com/myokit/myokit/archive/refs/tags/v1.39.1.tar.gz"

    # notify when the package is updated.
    maintainers("finsberg")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("MIT", checked_by="finsberg")

    version("main", branch="main")
    version("1.39.1", sha256="5d9abfc419aa56ffaa65c96e8a50283399e918606249c0651afe6f6c3216957a")

    # Python version and Build backend
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@64.0:", type=("build", "run"))

    # Core dependencies
    depends_on("py-configparser", type=("build", "run"))
    depends_on("py-lxml", type=("build", "run"))
    depends_on("py-matplotlib@2.2:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
