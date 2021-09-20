# pyndv - National Vulnerability Database stream data downloader


[![Current version at PyPI](https://img.shields.io/pypi/v/pyndv.svg)](https://pypi.python.org/pypi/pyndv)
![Supported Python Versions](https://img.shields.io/pypi/pyversions/pyndv.svg)
![Software status](https://img.shields.io/pypi/status/pyndv.svg)
[![License: MIT](https://img.shields.io/pypi/l/pyndv.svg)](https://github.com/vit0r/pyndv/blob/master/LICENSE)
[![codecov](https://codecov.io/gh/vit0r/pyndv/branch/master/graph/badge.svg)](https://codecov.io/gh/vit0r/pyndv)
[![GitHub contributors](https://img.shields.io/github/contributors/vit0r/pyndv.svg)](https://github.com/vit0r/pyndv/graphs/contributors)

## Install

```bash
$ pip install pyndv
```

## Usage

```bash
$ pyndv
$ pyndv --help
$ pyndv -f recent -o output.json
$ pyndv -f modified -o output.json
$ docker-compose up
$ docker run --rm --mount type=bind,source=$(pwd),target=/tmp/data vit0r/pyndv
```