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


class PyTextualImage(PythonPackage):
    """Render images via Kitty's Terminal Graphics Protocol with Rich and Textual"""

    homepage = "https://github.com/lnqs/textual-image"
    pypi = "textual-image/textual_image-0.8.5.tar.gz"

    license("LGPL-3.0-or-later", checked_by="finsberg")

    maintainers("finsberg")

    version("0.8.5", sha256="43d4c0026a4f21fa255f41eac7b0fc1f7410a4c7bc9bf95b908bec901b0a8c3a")
    version("0.13.2", sha256="8ca0cee2bfcd7734de5b16a1936da226b77b745e28830d9cf2bc202cb70e43ee")

    depends_on("python@3.12:", type=("build", "run"))

    depends_on("py-setuptools", type="build", when="@:0.13")
    depends_on("py-wheel", type="build", when="@:0.13")

    depends_on("py-uv", type="build", when="@0.13:")

    depends_on("py-pillow", type=("build", "run"))
    depends_on("py-rich", type=("build", "run"))
