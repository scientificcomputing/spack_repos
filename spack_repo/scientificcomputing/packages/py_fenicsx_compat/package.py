# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFenicsxCompat(PythonPackage):
    """Cross-version compatibility helpers for py-fenics-dolfinx (FEniCSx)."""

    homepage = "https://scientificcomputing.github.io/fenicsx-compat/"
    url = "https://github.com/scientificcomputing/fenicsx-compat/archive/refs/tags/v0.3.0.tar.gz"
    git = "https://github.com/scientificcomputing/fenicsx-compat.git"

    maintainers("finsberg", "jorgensd")

    license("MIT", checked_by="finsberg")

    version("main", branch="main")
    version("0.2.0", sha256="e26e2fc4616dd665cd58a868cc55080aaf0260e60db4b7877768fc6e8f563d7e")
    version("0.3.0", sha256="1dd8d4f0ed7dcc56fe522d2380f82fa6b795fc316739475ddaafbf474ee0882d")
    version("0.4.0", sha256="3a6d1fb8e79b470c49e0ecf6184221743a77c5e91d15ddde61208dd23275c862")
    version("0.6.0", sha256="281bb20f8e3c81548b98140eb55bd286a72948bca4a432df3502bdd3c13ccb7e")
    version("0.7.0", sha256="e8ae4b8d79d695be166269b562da4b27a81e00c8c53d8a989ec3d868bf3da4b0")

    depends_on("python@3.12:", type=("build", "run"))

    depends_on("py-hatchling", type="build")

    depends_on("py-fenics-dolfinx@0.10:", type=("build", "run"))
    depends_on("py-fenics-dolfinx@main", when="@main", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
