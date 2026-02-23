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
#     spack install py-mri-toolkit
#
# You can edit this file again by typing:
#
#     spack edit py-mri-toolkit
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMriToolkit(PythonPackage):
    """MRI-toolkit provides a set of features dedicated to human MRI data post-processing"""

    homepage = "https://scientificcomputing.github.io/mri-toolkit"
    git = "https://github.com/scientificcomputing/mri-toolkit.git"

    url = "https://github.com/scientificcomputing/mri-toolkit/archive/refs/tags/v0.1.0.tar.gz"

    license("MIT", checked_by="finsberg")

    maintainers("finsberg", "cdaversin")

    version("main", branch="main")
    version(
        "0.1.0",
        sha256="729d6094ed6edbe513905cecb4609b5238d04e360c68c632ec32fba97bbd80b9",
    )

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-setuptools@61.2:", type="build")
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-rich-argparse", type=("build", "run"))
    depends_on("py-nibabel", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))

    variant("show", default=True, description="Show images in the terminal")
    with when("+show"):
        depends_on("py-pillow", type=("build", "run"))
        depends_on("py-matplotlib", type=("build", "run"))
        depends_on("py-textual-image", type=("build", "run"))

    variant("napari", default=True, description="Napari support")
    with when("+napari"):
        depends_on("py-napari", type=("build", "run"))
