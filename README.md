# Blog-Web

This is a Blog Website designed by me having Hatch as a python package manager and as a flask application


[![PyPI - Version](https://img.shields.io/pypi/v/blog-web.svg)](https://pypi.org/project/blog-web)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/blog-web.svg)](https://pypi.org/project/blog-web)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install blog-web
```

## License

`blog-web` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Common Commands
## in VENV
export PYTHONPATH=$(pwd)/src  
flask db migrate -m "Initial migration."
flask db upgrade

# in terminal to start postgres and other stuff (need to start services using brew postgres)
psql postgres         

\conninfo (to see which user)
CREATE DATABASE mydatabase;
CREATE USER postgres WITH ENCRYPTED PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO postgres;

\dt  (see tables created)
\c mydatabase  (connect to database)

GRANT ALL PRIVILEGES ON SCHEMA public TO postgres;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO postgres;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO postgres;