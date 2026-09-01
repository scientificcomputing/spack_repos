# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTyper(PythonPackage):
    """Typer, build great CLIs. Easy to code. Based on Python type hints."""

    homepage = "https://github.com/tiangolo/typer"
    pypi = "typer/typer-0.24.1.tar.gz"

    license("MIT", checked_by="finsberg")

    version("0.24.1", sha256="e39b4732d65fbdcde189ae76cf7cd48aeae72919dea1fdfc16593be016256b45")
    version("0.26.7", sha256="e314a34c617e419c091b2830dda3ea1f257134ff593061a8f5b9717ab8dddb3a")
    version("0.27.1", sha256="a79bef8469a79c45498e7b814ecf8d603cc7644e9acbd9e19cac0334240b18df")
    version("0.27.2", sha256="269b7eb9d3c202ca84b4bc9618cb04ebb43d3d4d1e567e4c768607232c05f945")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-pdm-backend", type="build")

    depends_on("py-click@8.2.1:", type=("build", "run"))
    depends_on("py-shellingham@1.3.0:", type=("build", "run"))
    depends_on("py-rich@12.3:", type=("build", "run"))
    depends_on("py-annotated-doc@0.0.2:", type=("build", "run"))
