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


class PyGotranx(PythonPackage):
    """Next generate ODE translator"""

    homepage = "https://finsberg.github.io/gotranx"

    url = "https://github.com/finsberg/gotranx/archive/refs/tags/v1.5.0.tar.gz"

    # notify when the package is updated.
    maintainers("finsberg")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("MIT", checked_by="finsberg")

    version(
        "1.5.0",
        sha256="5d9abfc419aa56ffaa65c96e8a50283399e918606249c0651afe6f6c3216957a",
    )
    version(
        "1.4.0",
        sha256="47d79462d5219cefe4d6346a68292f7504a11e46512f69dcd300a6413d1084e0",
    )

    # Python version and Build backend
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@61.2:", type="build")

    # Core dependencies
    depends_on("py-attrs", type=("build", "run"))
    depends_on("py-lark", type=("build", "run"))
    depends_on("py-pint", type=("build", "run"))
    depends_on("py-rich-click", type=("build", "run"))
    depends_on("py-structlog", type=("build", "run"))
    depends_on("py-sympy", type=("build", "run"))
    depends_on("py-typer", type=("build", "run"))
    depends_on("py-myokit", type=("build", "run"))

    # click < 8.2
    depends_on("py-click@:8.1", type=("build", "run"))

    # toml ; python_version < '3.11'
    depends_on("py-toml", type=("build", "run"), when="^python@:3.10")
