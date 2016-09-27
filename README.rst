State of the Art Python Library Cookiecutter
============================================

Cookie cutter recipe for bootstrapping a State of the Art Python library. "Library" means your
Python module is not an application, and might be used by other module to build a application.

The main difference between Python "Library" and "Application" is dependencies versioning: for a
library, you do not want to freeze all versions of your dependencies. For example, if your library A
depends on another module B in version 1.0 and if you freeze this version in the requirements.txt,
another library cannot say it needs another version, for example >=1.1.0.

On the other side, for application that does to production, you absolutly want to freeze **all**
dependencies. You do not want to have your deployment broken because a new version of a package that
broke your application has just appeared on Pypi.

See https://github.com/audreyr/cookiecutter for more information about Cookiecutter.

Features
--------

Feature of this Cookiecutter recipe:
- Library that supports Python 2.7, 3.4, 3.5, Pypy
- optional install a virtualenv for library developer
- Free software: MIT license
- Github host
- PBR: Set up to use Python Build Reasonableness
- separated production `requirements.txt` and development/test `requirements-dev.txt`
- Pylint, Yapf, Pep8: code style
- Travis-CI: for build and unit test
- Coverage: unit test report
- Tox testing: Setup to easily test for Python 2.6, 2.7, 3.3, 3.4
- Sphinx docs: Documentation ready for generation and publication to ReadTheDoc
- Pypi: automatic deployment of distribution package or wheels.

Usage
-----

Do not create a folder for your project, it will be automatically created.

Generate a Python package project:

.. code-block:: bash

    $ cookiecutter https://github.com/Stibbons/python-library-cookiecutter

Create a virtualenv:

.. code-block:: bash

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install --upgrade pip  # Force upgrade to latest version of pip

Setup for production:

.. code-block:: bash

    $ pip install -r requirements.txt .

Setup for development and unit tests

.. code-block:: bash

    $ pip install -r requirements.txt -r requirements-dev.txt -e .

Build source package:

.. code-block:: bash

    python setup.py sdist

Build binary package:

.. code-block:: bash

    python setup.py bdist

Build Wheel package:

.. code-block:: bash

    python setup.py bdist_wheel

Configuration
-------------

You will need to configure `.travis.yml` to enable automatic PyPi deployment
