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

echo "Setting up environment for testing..."\
# note: do NOT use --dev here, we want to use the "prod" cookiecutter
pipenv install

echo "Creating testdir"
cd $(dirname $0)
rm -rfv testdir
mkdir -p testdir

echo "Testing cookiecutter receipe..."
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


echo "Testing cookiecutter receipe..."
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

echo "Test went successful (in $PWD)"
