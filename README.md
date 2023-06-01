# mcph

[![Support Ukraine](https://badgen.net/badge/support/UKRAINE/?color=0057B8&labelColor=FFD700)](https://www.gov.uk/government/news/ukraine-what-you-can-do-to-help)

[![Build Status](https://github.com/PerchunPak/mcph/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/PerchunPak/mcph/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/PerchunPak/mcph/branch/master/graph/badge.svg)](https://codecov.io/gh/PerchunPak/mcph)
[![Documentation Build Status](https://readthedocs.org/projects/mcph/badge/?version=latest)](https://mcph.readthedocs.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python support versions badge (from pypi)](https://img.shields.io/pypi/pyversions/mcph)](https://www.python.org/downloads/)

Minecraft plugin helper, updates and checks versions of all plugins on a server!

# The project is archived

I have no interest in continuing the project, as I no longer build servers in Minecraft. While I could build such software well,
I just don't need this. If you want to use something same, look at [pluGET](https://github.com/Neocky/pluGET) (this is originally
their idea) or [mineflake](https://github.com/nix-community/mineflake) (same idea, but instead of managing already downloaded plugins,
you can build an entire container for the server, where every plugin is compiled from sources during the build!).

## Features

- Nice and powerful [documentation](https://mcph.readthedocs.io/en/latest/)!
- Easy management plugins in simple commands!
- Easy readable and supportable code!
- Support for Spigotmc.org plugins!

## Installing

```bash
pip install mcph
```

## Installing for local developing

```bash
git clone https://github.com/PerchunPak/mcph.git
cd mcph
```

### Installing `poetry`

Next we need install `poetry` with [recommended way](https://python-poetry.org/docs/master/#installation).

If you use Linux, use command:

```bash
curl -sSL https://install.python-poetry.org | python -
```

If you use Windows, open PowerShell with admin privileges and use:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### Installing dependencies

```bash
poetry install --no-dev
```

### Configuration

All configuration happens in `config.yml`, or with enviroment variables.

### If something is not clear

You can always write me!

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

## Updating

For updating, just run `pip install -U mcph`. Or if you installed this for developing - `git pull`.

## Thanks

This project was generated with [fire-square-style](https://github.com/fire-square/fire-square-style).
