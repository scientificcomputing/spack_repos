# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFestim(PythonPackage):
    """FESTIM (Finite Elements Simulation of Tritium in Materials) is a tool
    for modeling hydrogen transport in materials. It simulates the diffusion
    and trapping of hydrogen, coupled to heat transfer with FEniCS."""

    homepage = "https://festim.readthedocs.io/en/latest/"
    url = "https://github.com/festim-dev/FESTIM/archive/refs/tags/v2.0-beta.2post1.tar.gz"
    git = "https://github.com/festim-dev/FESTIM.git"

    maintainers("jorgensd")

    license("Apache-2.0", checked_by="jorgensd")

    version("main", branch="fenicsx")
    version(
        "2.0-beta.2post1",
        sha256="d1ebca798f975480289b8027c5ff87a8bd3b21b8931f09660614fdd9d80c7819",
    )
    version(
        "2.0-alpha.8", sha256="b12144204e6d1d887a9c0cfadafbfaa87aa6b16fc09f0884df72fe6d0d56dc38"
    )
    version(
        "2.0-alpha.8", sha256="b12144204e6d1d887a9c0cfadafbfaa87aa6b16fc09f0884df72fe6d0d56dc38"
    )

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@42:", type="build")

    depends_on("py-scifem@0.4.0:", type="run")

    depends_on("py-adios4dolfinx@0.10", when="@2.0-beta.2post1", type="run")
    depends_on("py-adios4dolfinx@main", when="@main", type="run")

    depends_on("py-fenics-dolfinx@0.10+petsc4py", when="@2.0-beta.2post1", type="run")
    depends_on("py-fenics-dolfinx@main+petsc4py", when="@main", type="run")

    depends_on("fenics-dolfinx+adios2", type="run")

    depends_on(
        "hdf5@1.12:", type="build"
    )  # NOTE: Remove when https://github.com/spack/spack-packages/issues/3566 is resolved
    depends_on("petsc+mumps", type="run")

    depends_on("py-numpy", type="run")
    depends_on("py-sympy", type="run")
    depends_on("py-tqdm", type="run")
