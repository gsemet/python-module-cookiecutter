===============================
{{ cookiecutter.library_name }}
===============================

{{ cookiecutter.project_short_description}}

* Free software: MIT
* Documentation: {{ cookiecutter.library_name }}.readthedocs.org/en/latest/
* Source: {{ cookiecutter.author_website }}

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

    $ pip install -r requirements.txt -e .
    $ pip install -r requirements-dev.txt

Build source package:

.. code-block:: bash

    python setup.py sdist

Build binary package:

.. code-block:: bash

    python setup.py bdist

Build Wheel package:

.. code-block:: bash

    python setup.py bdist_wheel
