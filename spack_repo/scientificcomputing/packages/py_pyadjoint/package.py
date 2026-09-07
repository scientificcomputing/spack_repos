# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyadjoint(PythonPackage):
    """Pyadjoint is a Python library for automatic differentiation."""

    homepage = "https://github.com/dolfin-adjoint/pyadjoint"
    url = "https://github.com/dolfin-adjoint/pyadjoint/archive/refs/tags/2026.4.1.tar.gz"
    git = "https://github.com/dolfin-adjoint/pyadjoint.git"

    maintainers("finsberg", "jorgensd")

    license("LGPL-3.0-only", checked_by="finsberg")

    version("main", branch="main")
    version("2026.4.1", sha256="425d8061311fd32cbd82c94bfd7ec8c75421d39d020cbb2940ac94cc700264bd")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")

    depends_on("py-checkpoint-schedules", type=("build", "run"))
    depends_on("py-scipy@1:", type=("build", "run"))
    depends_on("py-sympy", type=("build", "run"))
