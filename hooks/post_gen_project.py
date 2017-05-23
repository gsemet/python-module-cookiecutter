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
        print("Setting up a virtual environment")
        pyversion = "--three"
        if '{{ cookiecutter.python_version }}' == '2':
            pyversion = "--two"
        subprocess.check_call(["pipenv", pyversion])
        subprocess.check_call(["pipenv", "install", "--dev"])

        print("Initial build...")
        venv = subprocess.check_output(["pipenv", "--venv"]).strip().decode('utf8')
        # Cannot use directly `pipenv run`, it requires a TTY, and the
        # --no-interactive options is not available on every version
        subprocess.check_call([os.path.join(venv,
                                            "bin",
                                            "python"), "setup.py", "sdist"])

        print("Developer environment created. Activate with:")
        print("  pipenv shell")
