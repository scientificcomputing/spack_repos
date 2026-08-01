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
    """General ODE translator"""

    homepage = "https://finsberg.github.io/gotranx"
    git = "https://github.com/finsberg/gotranx.git"
    url = "https://github.com/finsberg/gotranx/archive/refs/tags/v1.5.1.tar.gz"

    # notify when the package is updated.
    maintainers("finsberg")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("MIT", checked_by="finsberg")

    version("main", branch="main")
    version("1.5.1", sha256="5386876d6cd6f4465a8288a27a7fd44a98116e5b7887173578873371a6a4d3a6")
    version("1.6.1", sha256="43602fb6782b33774a119d35545a99ad27cf9a76fbe919844a1f42b5e20cc1e8")
    version("1.8.0", sha256="05c4f724a12119cda89eb69d82ebb8f3ed3935e9e1bdc2bf408a75adfda11b1d")

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
    depends_on("py-typer@0.15.4:", type=("build", "run"))
    depends_on("py-myokit", type=("build", "run"))

    # click < 8.2
    depends_on("py-click", type=("build", "run"))

    # toml ; python_version < '3.11'
    depends_on("py-toml", type=("build", "run"), when="^python@:3.10")
