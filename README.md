# gitsync

![ci_workflow](https://github.com/edijon/gitsync/actions/workflows/python-app.yml/badge.svg)

* Allows to synchronize remote `git` repositories locally.
* Aims to be a python training to me.
* Currently works for Github/Gitlab user repositories only. 
    > tested on public repositories.
* You are free to use it on your own risk.


## How to set-up

- Get dependencies
    ```bash
    pip install .
    ```

## Usage

* Command Line Interface 
* Getting help
    ```bash
    python3 -m gitsync --help
    ```
* Exemple :
    ```bash
    python3 -m gitsync edijon /tmp/ --provider=github 
    ```

## Testing

* You can use `pytest`
    ```bash
    pytest
    ```
