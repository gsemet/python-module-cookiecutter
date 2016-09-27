#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import subprocess


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if '{{ cookiecutter.use_pypi_deployment_with_travis }}' != 'y':
        remove_file('travis_pypi_setup.py')

    print("Creating git repository (needed for PBR to fully work)")
    subprocess.check_call(["git", "init", "."])

    if '{{ cookiecutter.create_developer_env_after_scapfolding }}' == 'y':
        print("Setting up a virtual environment in {}/venv".format(PROJECT_DIRECTORY))
        subprocess.check_call(["virtualenv", "venv"])
        subprocess.check_call(["venv/bin/pip", "install", "--upgrade", "pip"])

        subprocess.check_call(["venv/bin/pip", "install", "-r", "requirements.txt", "-e", "."])
        subprocess.check_call(["venv/bin/pip", "install", "-r", "requirements-dev.txt"])

        print("Initial build...")
        subprocess.check_call(["venv/bin/python", "setup.py", "sdist"])

        print("Developer environment created. Source it with: ")
        print("  cd {}".format(PROJECT_DIRECTORY))
        print("  source venv/bin/activate")
