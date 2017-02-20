# Environment Management

Similar to pip, conda is an open source package and environment management system [^1]. Anaconda is a data science platform that comes with a lot of packages. It uses conda at the core. Unlike Anaconda, Miniconda doesn't come with any installed packages by default. Note that for miniconda, everytime you open up a terminal, conda won’t automatically be available. Run the command below to use conda within miniconda.

# Conda

Let’s first start by checking if conda is installed.

```
$ conda --version

conda 4.2.12
```

To see the full documentation for any command, type the command followed by --help. For example, to learn about the conda update command:

```
$ conda update --help
```

Once it has been confirmed that conda has been installed, we will now make sure that it is up to date.

```
$ conda update conda

Using Anaconda Cloud api site https://api.anaconda.org
Fetching package metadata: ....
.Solving package specifications: .........

Package plan for installation in environment //anaconda:

The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    conda-env-2.6.0            |                0          601 B
    ruamel_yaml-0.11.14        |           py27_0         184 KB
    conda-4.2.12               |           py27_0         376 KB
    ------------------------------------------------------------
                                           Total:         560 KB

The following NEW packages will be INSTALLED:

    ruamel_yaml: 0.11.14-py27_0

The following packages will be UPDATED:

    conda:       4.0.7-py27_0 --> 4.2.12-py27_0
    conda-env:   2.4.5-py27_0 --> 2.6.0-0
    python:      2.7.11-0     --> 2.7.12-1
    sqlite:      3.9.2-0      --> 3.13.0-0

Proceed ([y]/n)? y

Fetching packages ...
conda-env-2.6. 100% |################################| Time: 0:00:00 360.78 kB/s
ruamel_yaml-0. 100% |################################| Time: 0:00:00   5.53 MB/s
conda-4.2.12-p 100% |################################| Time: 0:00:00   5.84 MB/s
Extracting packages ...
[      COMPLETE      ]|###################################################| 100%
Unlinking packages ...
[      COMPLETE      ]|###################################################| 100%
Linking packages ...
[      COMPLETE      ]|###################################################| 100%
```

# Environments

## Create

In order to manage environments, we need to create at least two so you can move or switch between them. To create a new environment, use the conda create command, followed by any name you wish to call it:

```
# create new environment
conda create -n <your_environment> python=2.7.11
```

## Clone

Make an exact copy of an environment by creating a clone of it. Here we will clone snowflakes to create an exact copy named flowers:

```
conda create --name flowers --clone snowflakes
```

## List

**List all environments**

Now you can use conda to see which environments you have installed so far. Use the conda environment info command to find out

```
$ conda info -e

conda environments:
snowflakes            /home/username/miniconda/envs/snowflakes
bunnies               /home/username/miniconda/envs/bunnies
```

**Verify current environment**

Which environment are you using right now – snowflakes or bunnies? To find out, type the command:

```
conda info --envs
```

## Remove

If you didn’t really want an environment named flowers, just remove it as follows:

```
conda remove --name flowers --all
```

## Share

You may want to share your environment with another person, for example, so they can re-create a test that you have done. To allow them to quickly reproduce your environment, with all of its packages and versions, you can give them a copy of your environment.yml file.

**Export the environment file**

To enable another person to create an exact copy of your environment, you will export the active environment file.

```
conda env export > environment.yml
```

**Use environment from file**

Create a copy of another developer’s environment from their environment.yml file:

```
conda env create -f environment.yml
```

```
# remove environment
conda remove -n <your_environemnt> --all
```


[^1]: [Conda, Managing environments](http://conda.pydata.org/docs/using/envs.html#create-an-environment)