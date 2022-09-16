# mcph

[![Build Status](https://github.com/PerchunPak/mcph/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/PerchunPak/mcph/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/PerchunPak/mcph/branch/master/graph/badge.svg)](https://codecov.io/gh/PerchunPak/mcph)
[![Documentation Build Status](https://readthedocs.org/projects/mcph/badge/?version=latest)](https://mcph.readthedocs.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python Version](https://img.shields.io/pypi/pyversions/mcph.svg)](https://pypi.org/project/mcph/)

Minecraft plugin helper, updates and checks versions of all plugins on a server!

# Project in developing! Please do not use it!

At now implemented only output of plugins names and their versions.

## Features

- Nice and powerful [documentation](https://mcph.readthedocs.io/en/latest/)!
- Easy management plugins in simple commands!
- Easy readable and supportable code!
- Support for Spigotmc.org plugins!


## Installation

```bash
pip install mcph
```


## Example

Check updates for all plugins:

```bash
~ $ mcph check all .

┌────────────────────────────────────────────────────────────────────────────────┐
│ Num │        Name        │  Current Version  │ Last Version │ Update Available │
+─────+────────────────────+───────────────────+──────────────+──────────────────+
│  1  │       AuthMe       │ 5.6.0-beta2-b2453 │ 5.6.0-beta2  │      False       │
│  2  │      ClearLag      │       3.2.2       │    v3.2.2    │      False       │
│  3  │        CMI         │      9.0.2.9      │   1.1.2.4    │       True       │
│  4  │       CMILib       │      1.0.3.11     │   1.1.2.4    │       True       │
│  5  │    CoreProtect     │        20.1       │     21.2     │       True       │
│  6  │ FastAsyncWorldEdit │  1.17-380;ee0d1b5 │  Not Found   │       None       │
│  7  │   Geyser-Spigot    │   1.4.3-SNAPSHOT  │  Not Found   │       None       │
│  8  │     LuckPerms      │       5.3.74      │    5.4.0     │       True       │
└────────────────────────────────────────────────────────────────────────────────┘
```

## Thanks

## Credits

This project was generated with [`fire-square-style`](https://github.com/fire-square/fire-square-style). 
Current template version is: [9a4d61b1d3707090a14f5ad88291d7b892ae4292](https://github.com/fire-square/fire-square-style/tree/9a4d61b1d3707090a14f5ad88291d7b892ae4292). 
See what is [updated](https://github.com/fire-square/fire-square-style/compare/9a4d61b1d3707090a14f5ad88291d7b892ae4292...master) 
since then.
