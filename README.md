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

## Contributing
We welcome contributions to this project! If you have a new package or you want to improve the existing ones, please follow the steps in [CONTRIBUTING.md](CONTRIBUTING.md).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.