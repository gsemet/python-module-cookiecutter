===============================
{{ cookiecutter.library_name }}
===============================

.. image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}.svg?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}
.. image:: https://readthedocs.org/projects/{{ cookiecutter.library_name }}/badge/?version=latest
   :target: http://{{ cookiecutter.library_name }}.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.library_name }}/badge.svg
   :target: https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.library_name }}
.. image:: https://badge.fury.io/py/{{ cookiecutter.library_name }}.svg
   :target: https://pypi.python.org/pypi/{{ cookiecutter.library_name }}/
   :alt: Pypi package
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: ./LICENSE
   :alt: MIT licensed

{{ cookiecutter.project_short_description}}

* Free software: MIT
* Documentation: https://{{ cookiecutter.library_name }}.readthedocs.org/en/latest/
* Source: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}

Features
--------

* TODO

Usage
-----

* TODO


Note: only dependencies described in `requirements.txt` will be installed when
using `pip install`. The development dependencies (pylint,...) and **not**
installed on deployment.


Contributing
------------

Create a virtualenv:

    This will isolate your environment from the system environment.

    .. code-block:: bash

        $ virtualenv venv
        $ source venv/bin/activate
        $ pip install --upgrade pip  # Force upgrade to latest version of pip

Setup for production:

    This will only install production dependencies. You cannot run the unit test or do any code
    housework!

    .. code-block:: bash

        $ pip install -r requirements.txt .

Setup for development and unit tests:

    Full power environment.

    .. code-block:: bash

        $ pip install -r requirements.txt -r requirements-dev.txt -e .

Build source package:

    Use it for most package without low level system dependencies.

    .. code-block:: bash

        python setup.py sdist

Build binary package:

    Needed for package with a C or other low level source code.

    .. code-block:: bash

        python setup.py bdist

Build Wheel package:

    Always provide a wheel package.

    .. code-block:: bash

        python setup.py bdist_wheel

(Only for package owner)

Register and publish your package to Pypi:

    Do it locally only once, to create your package on `pypi.python.org`.

    .. code-block:: bash

        python setup.py sdist register upload

Create a release:

    Go on GitHub and create a tag with a semver syntax. Optionally you can tag code locally and push
    to GitHub.

    .. code-block:: bash

        git tag 1.2.3

    On successful travis build on the Tag branch, your Pypi package will be updated automatically.

