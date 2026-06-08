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


class PyStructlog(PythonPackage):
    """General ODE translator"""

    homepage = "https://github.com/hynek/structlog"

    url = "https://github.com/hynek/structlog/archive/refs/tags/25.5.0.tar.gz"

    # notify when the package is updated.
    maintainers("finsberg")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("MIT", checked_by="finsberg")

    version("main", branch="main")
    version("25.5.0", sha256="ca447e91f03a18b3ae1f1917342c023091e923418409e19cfe67b90dbdce2694")
    version("26.1.0", sha256="a32b711804f80404b1c6de47556df2215c399acec2d38199e91ceb4a2ca1fd51")

    # Python version and Build backend
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-vcs", type="build")
    depends_on("py-hatch-fancy-pypi-readme@22.8.0:", type="build")

    depends_on("py-typing-extensions", type=("build", "run"), when="^python@:3.11")
