#!/bin/bash

# On Ubuntu, ensure virtualenv is >= 12.0.2
if [ -f /etc/lsb-release ]; then
    grep "Ubuntu" /etc/lsb-release 2> /dev/null > /dev/null
    if [ $? == 0 ]; then
        MAJOR=$(pip show virtualenv | grep 'Version:' | cut -d':' -f2 | sed "s/ //g" | cut -d'.' -f 1)
        if [[ $MAJOR < 12 ]]; then
            echo "Need to update virtualenv ! Please execute:"
            echo "    pip install -U virtualenv>=12.0.2"
            exit 1
        fi
    fi
fi

if [[ $(pipenv --venv) != "" ]]; then
    echo "Existing Virtualenv: $(pipenv --venv)"
else
    echo "Creating Virtualenv"
    pipenv --three
fi


only=
if [[ "$1" == "docker_app" ]]; then
    only="docker_app"
elif [[ "$1" = "library" ]]; then
    only="library"
fi

set -xe

echo "Setting up environment for testing..."\
# note: do NOT use --dev here, we want to use the "prod" cookiecutter
python3 -m pip install --user --upgrade pip==19.0.2 pipenv==2018.11.26
pipenv install

echo "Creating testdir"
cd $(dirname $0)
rm -rf testdir
mkdir -p testdir

if [[ -z $only ]] || [[ $only == "docker_app" ]]; then
    echo "Testing docker_app..."
    echo "pwd: $PWD"
    pipenv run cookiecutter -v . -o testdir/docker_app << EOF
Author Name
author.name@server.com
y
project name
Short Project Description
project_slug
github_username
github_repository_name
pypi_username
y
y
y

EOF
    (
        cd testdir/docker_app/project_slug
        make style checks tests
    )
fi


if [[ -z $only ]] || [[ $only == "library" ]]; then
    echo "Testing library..."
    echo "pwd: $PWD"
    pipenv run cookiecutter -v . -o testdir/library << EOF
Author Name
author.name@server.com
n
project name
Short Project Description
project_slug
github_username
github_repository_name
pypi_username
n
y
y

EOF

    (
        cd testdir/library/project_slug
        make style checks tests
    )

    echo "Test went successful (in $PWD)"
fi
