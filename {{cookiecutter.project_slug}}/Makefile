.PHONY: build

MODULE:={{ cookiecutter.project_slug }}

all: dev style checks requirements build dists test-unit

dev:
	pipenv install --dev --skip-lock

install-local:
	pipenv install --skip-lock

install-system:
	pipenv install --system

style: isort autopep8 yapf

isort:
	pipenv run isort -y

autopep8:
	pipenv run autopep8 --in-place --recursive setup.py $(MODULE)

yapf:
	pipenv run yapf --style .yapf --recursive -i $(MODULE)

checks: sdist flake8 pylint

flake8:
	pipenv run python setup.py flake8

pylint:
	pipenv run pylint --rcfile=.pylintrc --output-format=colorized $(MODULE)

build: dists

shell:
	pipenv shell

test-unit:
	pipenv run pytest $(MODULE)

test-coverage:
	pipenv run py.test -v --cov $(MODULE) --cov-report term-missing

requirements:
	# needed until PBR supports `Pipfile`
	pipenv run pipenv_to_requirements

dists: requirements sdist bdist wheels

sdist:
	pipenv run python setup.py sdist

bdist:
	pipenv run python setup.py bdist

wheels:
	pipenv run python setup.py bdist_wheel

pypi-publish: build
	pipenv run python setup.py upload -r pypi

update:
	pipenv update

githook: style requirements

push: githook
	git push origin --all
	git push origin --tags

# aliases to gracefully handle typos on poor dev's terminal
check: checks
devel: dev
develop: dev
dist: dists
install: install-system
pypi: pypi-publish
styles: style
test: test-unit
unittest: test-unit
wheel: wheels
