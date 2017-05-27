===============================
{{ cookiecutter.project_name }}
===============================

.. image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}.svg?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}
.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_name }}/badge/?version=latest
   :target: http://{{ cookiecutter.project_name }}.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/badge.svg
   :target: https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}
.. image:: https://badge.fury.io/py/{{ cookiecutter.project_name }}.svg
   :target: https://pypi.python.org/pypi/{{ cookiecutter.project_name }}/
   :alt: Pypi package
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: ./LICENSE
   :alt: MIT licensed

{{ cookiecutter.project_short_description}}

* Free software: MIT
* Documentation: https://{{ cookiecutter.project_name }}.readthedocs.org/en/latest/
* Source: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}

Features
--------

* TODO

Usage
-----

* TODO


Note: See `pipenv documentation <https://github.com/kennethreitz/pipenv>`_ for Pipfile
specification.

Contributing
------------

Create your environment with

    .. code-block:: bash

        $ pipenv --three

PS: you can use `pipenv --two` for Python 2.


Setup for development and unit tests:

    .. code-block:: bash

        $ pipenv install --dev

Note

    Setup for production can be done with:

    .. code-block:: bash

        $ pipenv install

    But if your application uses this library through a `requirements.txt` (Pip) or through a
    `Pipfile` (Pipenv), you should not have to do this "setup for production" command.

Activate the environment:

    .. code-block:: bash

        $ pipenv shell

Execute a command directly inside the environment:

    .. code-block:: bash

        $ pipenv run ...

Execute unit tests:

    .. code-block:: bash

        $ pipenv run pytest test

Build source package:

    Use it for most package without low level system dependencies.

    .. code-block:: bash

        pipenv run python setup.py sdist

Build binary package:

    Needed for package with a C or other low level source code.

    .. code-block:: bash

        pipenv run python setup.py bdist

Build Wheel package:

    Always provide a wheel package.

    .. code-block:: bash

        pipenv run python setup.py bdist_wheel

(Only for package owner)

Register and publish your package to Pypi:

    Do it locally only once, to create your package on `pypi.python.org`.

    .. code-block:: bash

        pipenv run python setup.py sdist register upload

Create a release:

    Go on GitHub and create a tag with a semver syntax. Optionally you can tag code locally and push
    to GitHub.

    .. code-block:: bash

        git tag 1.2.3

    On successful travis build on the Tag branch, your Pypi package will be updated automatically.
