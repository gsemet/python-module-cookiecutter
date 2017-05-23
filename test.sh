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

set +e

pipenv install

echo "Creating testdir"
cd $(dirname $0)
rm -rfv testdir
mkdir -p testdir
cd testdir

cookiecutter .. << EOF
3
Author Name
author.name@server.com
library_name
Short Project Description
library_name
github_username
pipy_username
github_repository_name
y
y

EOF || exit 1

echo "Test went successful (in $PWD)"
