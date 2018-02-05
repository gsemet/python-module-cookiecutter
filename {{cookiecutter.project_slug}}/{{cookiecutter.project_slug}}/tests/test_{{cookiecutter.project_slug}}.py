#!/usr/bin/env python
# coding: utf-8

"""
test_{{ cookiecutter.project_slug }}
----------------------------------
Tests for `{{ cookiecutter.project_slug }}` module.
"""

# Third Party Libraries
import logging
import pytest

# {{ cookiecutter.project_name }} Modules
# from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}

# pylint: disable=redefined-outer-name, unused-argument

log = logging.getLogger(__name__)

@pytest.fixture
def setup_000(mocker):
    # mocker.patch("module.to.patchsleep")
    yield


def test_000_something(setup_000):
    pass
