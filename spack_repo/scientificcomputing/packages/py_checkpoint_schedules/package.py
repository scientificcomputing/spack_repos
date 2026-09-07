# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCheckpointSchedules(PythonPackage):
    """Schedules for incremental checkpointing of adjoint simulations."""

    homepage = "https://www.firedrakeproject.org/checkpoint_schedules/"
    url = (
        "https://github.com/firedrakeproject/checkpoint_schedules/archive/refs/tags/v1.0.4.tar.gz"
    )
    git = "https://github.com/firedrakeproject/checkpoint_schedules.git"

    maintainers("finsberg", "jorgensd")

    license("LGPL-3.0-only", checked_by="finsberg")

    version("1.0.4", sha256="b62a9b00c6b98a983f85f4c76bcf0262e50e7dcd1b9fde986d52a29172c6a1f8")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@61:", type="build")

    depends_on("py-numpy", type=("build", "run"))
