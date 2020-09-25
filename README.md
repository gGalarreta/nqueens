# nqueens

[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Build Status](https://travis-ci.org/ali-irawan/xtra.svg?branch=master)](https://travis-ci.com/gGalarreta/nqueens.svg?branch=master)
![alt text](https://github.com/gGalarreta/nqueens/blob/master/static/home.png)

## Prerequisities
You need the next aplication installed and open to run the project
```bash
docker
docker-compose
```

## Recommendation
You could use a virtual environment to have a better experience running the project


# Getting Started

## Docker Setup
```bash
docker-compose build
docker-compose up
```

## Server available

```bash
http://0.0.0.0:4000/
```

## Usage

For get a specific solution for a board size
```bash
http://localhost:4000/nqueens/backtraking/4
```

For get a full solution between a range of board size
```bash
http://localhost:4000nqueens/backtraking/range_solution/4/8
```
