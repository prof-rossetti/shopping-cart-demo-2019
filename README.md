# Shopping Cart Project

A demo version of the "Shopping Cart" project, for student reference.

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation

Fork this repository under your own control, then clone or download the resulting repository onto your computer. Then navigate there from the command line:

```sh
cd shopping-cart-demo-2019
```

> NOTE: subsequent usage and testing commands assume you are running them from the repository's root directory.

Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env". 

```sh
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env
```


## Usage

Run the program:

```py
python shopping_cart.py
```

## Testing

From within the virtual environment, install the `pytest` package (first time only):

```sh
pip install pytest
```

Run tests:

```py
pytest
```
