#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.project_slug }}
----------------------------------
Tests for `{{ cookiecutter.project_slug }}` module.
"""

{% if cookiecutter.use_pytest == 'y' -%}
from unittest import TestCase

import pytest
{% else %}
import sys

from unittest import TestCase
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' -%}
# note: use `asynctest.TestCase` instead of `unittest.TestCase` for your tests running inside
# the asyncio loop.
# Tests that do not use asyncio should still inherit from `unittest.TestCase`.
#
# uncomment the following string to use asyncio in your tests
# from asynctest import TestCase
{%- endif %}
from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}


class Test{{ cookiecutter.project_slug|title }}(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

{% if cookiecutter.use_pytest == 'n' -%}
if __name__ == '__main__':
    sys.exit(unittest.main())
{%- endif %}
