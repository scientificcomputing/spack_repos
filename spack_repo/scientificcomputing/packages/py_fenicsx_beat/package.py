# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFenicsxBeat(PythonPackage):
    """Library to run cardiac EP simulations in FEniCSx"""

    homepage = "https://finsberg.github.io/fenicsx-beat/"
    url = "https://github.com/finsberg/fenicsx-beat/archive/refs/tags/v0.2.3.tar.gz"
    git = "https://github.com/finsberg/fenicsx-beat.git"

    maintainers("finsberg")

    license("MIT", checked_by="finsberg")

    version("main", branch="main")
    version("0.2.4", sha256="ddba1ee2a4ded52a846b1ee11b1bd6e7d97522608dd6206436ae0fd58b12b17b")
    version("0.3.0", sha256="4dd8fefa122f86705945a6e2e5969dbf2a0fe987072b2a27f1298547717222a6")
    version("0.5.0", sha256="696f98fca69fd3e43474c83b72510481aef0e54cb99f789dfca32519f073bf39")
    version("0.6.0", sha256="e66fea0202e55b7d77850ff92ea8e5e12a2b9be54f1bb47003c0d389346c0420")
    version("0.7.2", sha256="7693829f66fb7971a68fcda4f32c414ea110622f74ab20144e8bcf362ee5eae9")
    version("0.8.0", sha256="6d01fc5801a997b583517c8f6e96bbb38329d472533181b532634c7d0a871c29")
    version("0.9.0", sha256="190fa5b83d590f0e395159cb73b72ee4844a6c06c0d37d91b3dc11f6232f3ef0")

    variant(
        "cardiac-geometries", default=True, description="Add cardiac geometries as a dependency"
    )
    variant(
        "cli",
        default=False,
        when="@0.7:",
        description="Dependencies of the TOML-config-driven `beat` command line interface",
    )

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-setuptools@42:", type="build")

    depends_on("py-fenics-dolfinx+petsc4py", type=("build", "run"))
    depends_on("py-fenics-basix", type=("build", "run"))
    depends_on("py-fenics-ufl", type=("build", "run"))
    depends_on("py-mpi4py", type=("build", "run"))
    depends_on("py-scifem", type=("build", "run"))
    depends_on("petsc+mumps", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-rich", type=("build", "run"))
    depends_on("py-pint", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))

    with when("+cardiac-geometries"):
        depends_on("py-cardiac-geometriesx", type=("build", "run"))
        depends_on("py-cardiac-geometriesx@0.17:", type=("build", "run"), when="@0.9:")

    requires("+cardiac-geometries", when="+cli", msg="The beat CLI needs cardiac-geometriesx")

    with when("+cli"):
        depends_on("py-pydantic@2:", type=("build", "run"))
        depends_on("py-pydantic-pint", type=("build", "run"))
        depends_on("py-toml", type=("build", "run"))
        depends_on("py-gotranx", type=("build", "run"))
        depends_on("py-io4dolfinx", type=("build", "run"))
