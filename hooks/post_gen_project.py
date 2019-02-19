#!/usr/bin/env python3

import os
import subprocess


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    print("Creating git repository (needed for PBR to fully work)")
    subprocess.check_call(["git", "init", "."])

    if '{{ cookiecutter.add_git_remote_after_scapfolding }}' == 'y':
        subprocess.check_call(["git", "remote", "add", "origin",
            "https://github.com/"
            "{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}"
        ])
        print("Please ensure the creation of the following project in githab: "
            "{{ cookiecutter.github_username }}/{{ cookiecutter.github_repository_name }}")

    subprocess.check_call(["git", "add", ".*", "*"])
    subprocess.check_call(["git", "commit", "-m", 'Initial cookiecutter commit', "--all"])

    if '{{ cookiecutter.docker_build }}' == 'n':
        print("docker not required, removing docker related files")
        subprocess.check_call(["rm", "-fv", "Dockerfile", ".dockerignore"])

    print("Please execute 'make dev style' and amend the initial commit before first push!")
