Modern Python Module Cookiecutter
=================================

.. image:: https://travis-ci.org/gsemet/python-module-cookiecutter.svg?branch=master
    :target: https://travis-ci.org/gsemet/python-module-cookiecutter

Cookie cutter recipe for bootstrapping an state of the art Python module using free services and the
best "opensource" mindset.


TD;DR
-----
Pipenv + PBR + Travis + Auto Pipy publish + autoformatting (yapf, isort) + static checks (pylint,
flake8, mypy) + sphinx doc


Python Library Receipe Features
-------------------------------

See https://github.com/audreyr/cookiecutter for more information about Cookiecutter.

Feature of the "Python Library" Cookiecutter recipe:

- Use `Pipenv <https://github.com/pypa/pipenv>`_ to describe dependencies in ``Pipfile``
- Source code is hosted on **Github**
- Free software: **MIT license**
- **Badges** for Travis, Coverage, Pypi, ReadTheDoc
- handle automatic versioning derived from Git Tag with
  `PBR <https://docs.openstack.org/pbr/latest/>`_. It also automatic creates `ChangeLog` and
  `AUTHORS` files from Git history
- a **Makefile** allows easy daily-life for developers and maintainers
- **isort, Yapf, AutoPep8** code formatting
- **Pylint, Flake8, Mypy**: static checks
- **Editorconfig**: autoconfiguration of almost any editor
- build and unit test on **Travis-CI**
- Use **Pytest** for Unit testing
- automatic deployment to **Pypi** of distribution packages and wheels on successful build on a
  tagged commit ("Tag to release" principle)
- **Automatically set Travis CI deployment token** with `travis_pypi_setup.py` script
- **Coverage** unit test report
- **Sphinx docs**: Documentation ready for generation and publication to **ReadTheDoc**

Please note this cookiecutter does not support Python 2 intentionnaly.


Library vs Application
----------------------

It is important to differentiate a Python "Library" and a Python "Application". Each form have its
own life and should handle dependencies differently:

- To ensure stability and reproductibility of the deployment of an **Application**, a good practice
  is to **freeze the versions of all its dependencies** (both direct and indirect), so, no matter
  what happens for example on https://pypi.python.org, for example a new, buggy version of a
  package your application relies on might actually break your deployment.
  Without proper "frozen" dependencies management, you might get this dependency library deployed
  on production without any validation.

- A **Library** does not have any meaning alone, it is always used by at least an application.
  The dependencies of a library should not be frozen and should be defined using version
  ranges.
  For example, let's imagine your library depends on a module A in version 1.0. Your library is
  then used in an application that also depends on the same module A, but in version 1.2. The best
  way to handle this is to let libraries describe the range of supported versions, and let the
  package manager (Pip) find the best candidates.


Usage
-----

Do not create a folder for your project, it will be automatically created.

Boostrap your Python library:

    .. code-block:: bash

        $ pip3 install --user --upgrade pip pipenv cookiecutter

        $ cookiecutter https://github.com/gsemet/python-module-cookiecutter

        # or

        $ cookiecutter gh:gsemet/python-module-cookiecutter

Setup for development:

    .. code-block:: bash

        $ make dev

Execute unit tests:

    .. code-block:: bash

        $ make test

Build package (source, binary and wheels):

    Use it for most package without low level system dependencies.

    .. code-block:: bash

        make dists

To register Pipy deployment:

- commit your work!
- enable your project on Travis
- execute ``pipenv run python travis_pypi_setup.py``

Create a release:

    .. code-block:: bash

        make release
        git tag 1.2.3
        make push

On successful travis build on the Tag branch, your Pypi package will be updated automatically.

Configuration
-------------

You will need to configure `.travis.yml` to enable automatic PyPi deployment, or use the provided
`travis_pypi_setup.py` script.
