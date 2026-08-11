# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAnnotatedDoc(PythonPackage):
    """Document parameters, class attributes, return types,
    and variables inline, with Annotated."""

    homepage = "https://github.com/fastapi/annotated-doc"
    pypi = "annotated-doc/annotated_doc-0.0.4.tar.gz"

    license("MIT", checked_by="finsberg")

    version("0.0.4", sha256="fbcda96e87e9c92ad167c2e53839e57503ecfda18804ea28102353485033faa4")
    version("0.0.5", sha256="c7e58ce09192557605d8bbd92836d7e1d520ac9580096042c0bfd197efacf1bb")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-pdm-backend", type="build")
