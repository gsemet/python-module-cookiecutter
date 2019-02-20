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
    # Remember FIRST rules of Unit Tests:
    #    https://github.com/ghsukumar/SFDC_Best_Practices/wiki/F.I.R.S.T-Principles-of-Unit-Testing
    # Fast (all test shall be fast, for developers to accept running hundreds asap)
    # Independent (Follow the 3 A pattern: Arrange, Act, Assert, no run-of-order dependency)
    # Repeatable (no matter the environment, the result will always be the same)
    # Self-Validating (test result does not need human analysis)
    # Thorough (cover every use case and not aim for 100% code coverage, test corner cases)
    pass

@pytest.mark.integration_tests
def test_an_integration_test():
    # This test is an "integration test", ie, might depends on an external system, be slow
    # of not fully environment independent.
    # These tests are more subjects to become rotten faster than unit tests, and might cost
    # more and more over time, while unit test will cost zero as long as the code does not evolve.
    pass
