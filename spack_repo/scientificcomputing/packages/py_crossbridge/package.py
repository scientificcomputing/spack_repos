# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCrossbridge(PythonPackage):
    """Cardiac crossbridge models"""

    homepage = "https://computationalphysiology.github.io/crossbridge"
    url = "https://github.com/ComputationalPhysiology/crossbridge/archive/refs/tags/v0.3.0.tar.gz"
    git = "https://github.com/ComputationalPhysiology/crossbridge.git"

    maintainers("finsberg")

    license("MIT", checked_by="finsberg")

    version("main", branch="main")
    version("0.3.0", sha256="e09d0a37b7b9c777c6a244bca7be315292e6ea95a56506c280490ca20ee97b9b")
    version("0.2.0", sha256="c71335c8a49734a93cf3730160f0d552627c2c207d9505cbfe34669d5f4467fe")
    version("0.3.1", sha256="d96f0c55f8aee1f0370c917959c1942f40a30f3b94096af102b46276c58f4a82")

    variant(
        "fast",
        default=False,
        when="@0.3.0:",
        description="Use numba to speed up batched linear algebra",
    )

    # Python version and Build backend
    depends_on("python@3.11:", type=("build", "run"))
    depends_on("py-setuptools@61.0.0:", type="build")
    depends_on("py-wheel", type="build")

    # Core dependencies
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))

    with when("+fast"):
        depends_on("py-numba", type=("build", "run"))
