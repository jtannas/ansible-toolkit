# Docs Folder

This folder contains the documentation source files for the project and instructions relevant to them.

## Installation

Basic installation:
    ```$ pip install -e . ```

All the goodies:
    ```$ pip install -e .[All] ```

## Automatic Refresh
When working on the docs, it is helpful to have them update as you change them.
You can do this with sphinx-autobuild

```
$ sphinx-autobuild docs/ docs/_build/html
```
