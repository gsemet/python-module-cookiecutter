#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.project_slug }}
----------------------------------
Tests for `{{ cookiecutter.project_slug }}` module.
"""

import pytest
{% if cookiecutter.use_asyncio == 'y' -%}
# note: use `asynctest.TestCase` instead of `unittest.TestCase` for your tests running inside
# the asyncio loop.
# Tests that do not use asyncio should still inherit from `unittest.TestCase`.
#
# uncomment the following string to use asyncio in your tests
# from asynctest import TestCase
{%- endif %}
from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}


def test_{{ cookiecutter.project_slug }}():
    pass
