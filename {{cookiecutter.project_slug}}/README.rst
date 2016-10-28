===============================
{{ cookiecutter.library_name }}
===============================

{{ cookiecutter.project_short_description}}

* Free software: MIT
* Documentation: {{ cookiecutter.library_name }}.readthedocs.org/en/latest/
* Source: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}

Features
--------

* TODO

Usage
-----

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
