# awitree

A simple interface to [jstree](https://www.jstree.com/) with AnyWidget that
can be used both in Jupyter Notebook and Marimo


## Installation

```sh
pip install atest
```

or with [uv](https://github.com/astral-sh/uv):

```sh
uv add atest
```

## Development

Create and manage your own virtual environment:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
jupyter lab example.ipynb
```

The widget front-end code bundles it's JavaScript dependencies. After setting up Python,
make sure to install these dependencies locally:

```sh
npm install
```

While developing, you can run the following in a separate terminal to automatically
rebuild JavaScript as you make changes:

```sh
npm run dev
```
