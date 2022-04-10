# mc-plugin-helper

[![Build Status](https://github.com/PerchunPak/mc-plugin-helper/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/PerchunPak/mc-plugin-helper/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/PerchunPak/mc-plugin-helper/branch/master/graph/badge.svg)](https://codecov.io/gh/PerchunPak/mc-plugin-helper)
[![Documentation Build Status](https://readthedocs.org/projects/mc-plugin-helper/badge/?version=latest)](https://mc-plugin-helper.readthedocs.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python Version](https://img.shields.io/pypi/pyversions/mc-plugin-helper.svg)](https://pypi.org/project/mc-plugin-helper/)

Minecraft plugin helper, updates and checks versions of all plugins on a server!

# Project in developing! Please do not use it!

At now implemented only output of plugins names and their versions.

## Features

- Nice and powerful [documentation](https://mc-plugin-helper.readthedocs.io/en/latest/)!
- Easy management plugins in simple commands!
- Easy readable and supportable code!
- Support for Spigotmc.org plugins!


## Installation

```bash
pip install mc-plugin-helper
```


## Example

Check updates for all plugins:

```bash
> mc-plugin-helper check all .

┌─────────────────────────────────────────────────────────────┐
│ Num │        Name        │      Version      │ Last Version │
+─────+────────────────────+───────────────────+──────────────+
│  1  │       AuthMe       │ 5.6.0-beta2-b2453 │     None     │
│  2  │      ClearLag      │       3.2.2       │     None     │
│  3  │        CMI         │      9.0.2.9      │     None     │
│  4  │       CMILib       │      1.0.3.11     │     None     │
│  5  │    CoreProtect     │        20.1       │     None     │
│  6  │ FastAsyncWorldEdit │  1.17-380;ee0d1b5 │     None     │
│  7  │   Geyser-Spigot    │   1.4.3-SNAPSHOT  │     None     │
│  8  │     LuckPerms      │       5.3.74      │     None     │
└─────────────────────────────────────────────────────────────┘
```

## Thanks

## Credits

This project was generated with [`autodonate-plugin-template`](https://github.com/fire-squad/autodonate-plugin-template). 
Current template version is: [cc64ede4f27ca8e272bff0a42d3950d26bcacb9a](https://github.com/fire-squad/autodonate-plugin-template/tree/cc64ede4f27ca8e272bff0a42d3950d26bcacb9a). 
See what is [updated](https://github.com/fire-squad/autodonate-plugin-template/compare/cc64ede4f27ca8e272bff0a42d3950d26bcacb9a...master) 
since then.
