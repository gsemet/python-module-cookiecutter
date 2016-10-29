State of the Art Python Library Cookiecutter
============================================

Cookie cutter recipe for bootstrapping a State of the Art Python library. "Library" means your
Python module is not an application, and might be used by other module to build a application.

The main difference between Python "Library" and "Application" is how dependencies are versioned:
for a library, you do not want to freeze all versions of your dependencies. For example, if your
library A depends on another module B in version 1.0 and if you freeze this version in the
requirements.txt, another library cannot say it needs another version, for example >=1.1.0.

Libraries should handle dependencies using version ranges, not frozen version.

On the other side, for application that goes to production, you absolutly want to freeze **all**
dependencies. You do not want to have your deployment broken because a new version of a package that
broke your application has just appeared on Pypi.

See https://github.com/audreyr/cookiecutter for more information about Cookiecutter.

Features
--------

Feature of this Cookiecutter recipe:

- Github host
- Free software: MIT license
- Python 2.7, 3.4, 3.5, Pypy
- PBR: Set up to use Python Build Reasonableness, to handle automatic versioning based on Git Tag,
  automatic creation of `ChangeLog` and `AUTHORS` files.
- Optionally install a virtualenv for library developer
- Separated dev/prod requirements files:
    - `requirements.txt` for production
    - `requirements-dev.txt` for development/test
- Pylint, Yapf, Pep8: code style
- Coverage: unit test report
- Tox testing: Setup to easily test for Python 2.6, 2.7, 3.3, 3.4
- Travis-CI: for build, unit test and deploy tagged version to Pypi
- Sphinx docs: Documentation ready for generation and publication to ReadTheDoc
- Pypi: automatic deployment of distribution package or wheels.

Usage
-----

Do not create a folder for your project, it will be automatically created.

Generate a Python package project:

    Use Cookiecutter and this repository to save hours setting up your python library project.

    .. code-block:: bash

        $ cookiecutter https://github.com/Stibbons/python-library-cookiecutter

Create a virtualenv:

    .. code-block:: bash

        $ virtualenv venv
        $ source venv/bin/activate
        $ pip install --upgrade pip  # Force upgrade to latest version of pip


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

Configuration
-------------

You will need to configure `.travis.yml` to enable automatic PyPi deployment, or use the provided
`travis_pypi_setup.py` script. Beware your Yaml file will be overwritten, you will have to merge
it manually.
