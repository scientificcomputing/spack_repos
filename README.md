# spack_repos

Spack-repositories hosted by Scientific Computing, following: https://spack.readthedocs.io/en/latest/repositories.html

Clone and activate spack

```bash
. spack/share/spack/setup-env.sh
```

Create and activate a spack env

```bash
spack env create name-of-env
spack env activate name-of-env
```

To use the packages in this repo, add the `FEniCS` spack repos

```bash
spack repo add https://github.com/FEniCS/spack-fenics.git
```

then add this repository

```bash
spack repo add https://github.com/scientificcomputing/spack_repos.git
```

or clone it and add it

```bash
git clone https://github.com/scientificcomputing/spack_repos.git
spack repo add spack_repos/spack_repo/scientificcomputing

```

Then for instance add `pyscifem`

```bash
spack add py-scifem@0.16
```

Finally you can install the dependencies by first calling 
```
spack concretize
```
to resolve the potentially conflicting dependencies, and then install the packages with
```
spack install -j <number of cores>
```
e.g
```
spack install -j 4
```


## How to guides


### Checking out a specific version of a package

If you want to check out a specific branch, create new version, or edit an existing version of a package, you can use the `spack edit <name of package>` command, e.g
```
spack edit py-scifem
```
This will open the package.py file in your default editor, where you can make the necessary changes, for example say you want to check out a branch called `feature-x` you can add the following to the `version` section of the package.py file
```python
version("X.Y.Z.dev0", branch="feature-x")
```
where X.Y.Z is the latest release, and then use `spack add <name of package>@X.Y.Z.dev0`, e.g `spack add py-scifem@X.Y.Z.dev0` to add that specific branch to your spack environment. If you have an existing environment you can edit the config file using 
```
spack config edit
```
Next run 
```
spack concretize --fresh --force
```
and then 
```
spack install -j <number of cores>
```


## Contributing
We welcome contributions to this project! If you have a new package or you want to improve the existing ones, please follow the steps in [CONTRIBUTING.md](CONTRIBUTING.md).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.