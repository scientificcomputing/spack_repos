# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.packages.adios2.package import Adios2 as BuiltinAdios2

from spack.package import *


class Adios2(BuiltinAdios2):
    """ADIOS2 with the HDF5 VOL connector exposed in its own HDF5 plugin directory.

    The builtin package adds the whole lib directory to HDF5_PLUGIN_PATH, which in an
    environment view is the view's lib directory. HDF5 then dlopens every library in the
    view when h5py is imported, which segfaults when e.g. vtk is in the same view.
    Remove this override once that is fixed upstream in spack-packages.
    """

    @property
    def h5vol_plugin_dir(self):
        return join_path(self.prefix.lib, "hdf5-plugins")

    @run_after("install")
    def install_h5vol_plugin_dir(self):
        h5vol = find_libraries("libadios2_h5vol", root=self.prefix, recursive=True)
        if h5vol:
            mkdirp(self.h5vol_plugin_dir)
            symlink(
                os.path.relpath(h5vol[0], self.h5vol_plugin_dir),
                join_path(self.h5vol_plugin_dir, h5vol.basenames[0]),
            )

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        builtin_env = EnvironmentModifications()
        super().setup_run_environment(builtin_env)
        builtin_env.drop("HDF5_PLUGIN_PATH")
        env.extend(builtin_env)

        if os.path.isdir(self.h5vol_plugin_dir):
            env.prepend_path("HDF5_PLUGIN_PATH", self.h5vol_plugin_dir)
