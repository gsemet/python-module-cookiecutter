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


(Only for package owner)

Register on Pypi

.. code-block:: bash

    python setup.py register

Publish on Pypi

.. code-block:: bash

    python setup.py upload

