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


class PyCardiacGeometriesx(PythonPackage):
    """General ODE translator"""

    homepage = "https://computationalphysiology.github.io/cardiac-geometriesx"
    git = "https://github.com/ComputationalPhysiology/cardiac-geometriesx.git"
    url = "https://github.com/ComputationalPhysiology/cardiac-geometriesx/archive/refs/tags/v0.12.0.tar.gz"

    # notify when the package is updated.
    maintainers("finsberg")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("MIT", checked_by="finsberg")

    version("main", branch="main")
    version("0.12.0", sha256="93698a5d0d8ac7751c458dde963116a9c050c6d534b45cd034aa13dd668cc904")

    # Python version and Build backend
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@61.2:", type="build")

    # Core dependencies
    depends_on("py-fenics-dolfinx", type=("build", "run"))
    depends_on("py-rich-click", type=("build", "run"))
    depends_on("py-cardiac-geometries-core", type=("build", "run"))
    depends_on("py-structlog", type=("build", "run"))

    depends_on("py-io4dolfinx", type=("build", "run"), when="@main:")
    depends_on("py-adios4dolfinx", type=("build", "run"), when="@:0.12")
    depends_on("py-scifem", type=("build", "run"))
