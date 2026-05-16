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
    version("0.25.1", sha256="9616eb8853a09ffeabab1698952f33c6f29ffdbceb4eaeecf571880e8d7664cc")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-pdm-backend", type="build")

    depends_on("py-click@8.2.1:", type=("build", "run"))
    depends_on("py-shellingham@1.3.0:", type=("build", "run"))
    depends_on("py-rich@12.3:", type=("build", "run"))
    depends_on("py-annotated-doc@0.0.2:", type=("build", "run"))
