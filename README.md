# spack_repos

Spack-repositories hosted by Scientific Computing, following: https://spack.readthedocs.io/en/latest/repositories.html

Clone and activate spack

```bash
. spack/share/spack/setup-env.sh
```

Create and activate a spack env

```bash
spack env create name-of-env
spack activate name-of-env
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
