State of the Art Python Library Cookiecutter
============================================

Cookie cutter recipe for bootstrapping a State of the Art Python library. "Library" means your
Python module is not an application, and might be used by other module to build a application.

See https://github.com/audreyr/cookiecutter for more information about Cookiecutter.


Feature of this recipe:
- Free software: MIT license
- PBR: Set up to use Python Build Reasonableness
- Pylint, Yapf, Pep8: code style
- Travis: for build and unit test
- Coverage: unit test report
- Tox testing: Setup to easily test for Python 2.6, 2.7, 3.3, 3.4
- Sphinx docs: Documentation ready for generation and publication

Usage
-----

Generate a Python package project:

.. code-block:: bash

    cookiecutter https://github.com/Stibbons/python-library-cookiecutter


