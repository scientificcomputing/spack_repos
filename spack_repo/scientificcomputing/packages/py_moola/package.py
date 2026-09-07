# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMoola(PythonPackage):
    """Moola optimisation package."""

    homepage = "https://github.com/funsim/moola"
    url = "https://github.com/funsim/moola/archive/refs/tags/0.1.6.tar.gz"
    git = "https://github.com/funsim/moola.git"

    maintainers("finsberg", "jorgensd")

    license("LGPL-3.0-only", checked_by="finsberg")

    version("master", branch="master", preferred=True)
    version("0.1.6", sha256="dc8ff34a2aaf69d983ab718172402b965a1617e044ed795346a5d1de1816ed4d")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-numpy", type=("build", "run"))
