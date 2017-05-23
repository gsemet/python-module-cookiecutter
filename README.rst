State of the Art Python Library Cookiecutter
============================================

.. image:: https://travis-ci.org/Stibbons/python-library-cookiecutter.svg?branch=master
    :target: https://travis-ci.org/Stibbons/python-library-cookiecutter

Cookie cutter recipe for bootstrapping a State of the Art Python **library**. "Library" means your
Python module is not an application, and it needs to be used by at least one other module to build a
application.

Pyhton Python "Library" and "Application" is how dependencies are versioned:

- for a library, dependencies version should not be frozen. For example, let's imagine your library
  depends on a module A in version 1.0. Your library is used in an application that also depends on
  the same module A, but in version 1.2. The version installed will depends on which latest install
  script has been installed.
  Libraries should handle dependencies using version ranges, not frozen version.

- for application that goes to production, a great practice to set up is to ensure full
  reproductibility of your installation, no matter what happens on https://pypi.python.org. You
  absolutly want to freeze **all** dependencies. You do not want to have your deployment broken
  because a new version of a package that broke your application has just appeared on Pypi.

See https://github.com/audreyr/cookiecutter for more information about Cookiecutter.

Features
--------

Feature of this Cookiecutter recipe:

- **Github** host
- Free software: MIT license
- Python 2.7, 3.4, 3.5, Pypy
- use **Pipenv** to manage Pipfile, Pipfile.lock (upcoming Python standard)
- **PBR**: Set up to use Python Build Reasonableness, to handle automatic versioning based on Git Tag,
  automatic creation of `ChangeLog` and `AUTHORS` files
- **Pylint, Yapf, Pep8**: code style
- **Coverage**: unit test report
- **Pytest**: Setup to easily test for Python 2.6, 2.7, 3.3, 3.4
- **Travis-CI**: build, unit test and deploy tagged version to Pypi
- **Sphinx docs**: Documentation ready for generation and publication to ReadTheDoc
- **Pypi**: automatic deployment of distribution package or wheels on successful Travis build (tag).

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

Create a repository on Github, add a remote and push

.. code-block:: bash

    $ git remote add origin http://....
    $ git push origin

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
