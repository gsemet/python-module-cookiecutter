.PHONY: build docs mk-venv


# ==================================================================================================
# Variables
# ==================================================================================================

MODULES:={{ cookiecutter.project_slug }}
PACKAGE_NAME:={{ cookiecutter.project_slug }}
EXECUTABLE_NAME:={{ cookiecutter.project_slug }}

PIPENV:=pipenv
PYTHON:=$(shell which python3)
PIP:=$(PYTHON) -m pip
PIPENV_LOCK_ARGS:= --deploy --ignore-pipfile


# ==================================================================================================
# General Functions
# ==================================================================================================

define BROWSER_PYSCRIPT
import os, webbrowser, sys
from urllib.request import pathname2url
webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python3 -c "$$BROWSER_PYSCRIPT"

define PRINT_HELP_PYSCRIPT
import re, sys
for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-30s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


# ==================================================================================================
# help target
# ==================================================================================================

help:  ## This help message
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)


# ==================================================================================================
# do-it-all targets
# ==================================================================================================

all: dev style checks dists test  ## Build everything

dev: ensure-pipenv mk-venv pipenv-install-dev requirements  ## Setup dev environment

initial-dev: update style  ## Initial dev environment


# ==================================================================================================
# Install targets
# ==================================================================================================

ensure-pipenv:
	@if [ ! -z "$(VIRTUALENV)" ]; then \
		$(PIP) install --user --upgrade pip==18.1 pipenv==2018.10.9; \
		echo "ensure your local python install is in your PATH"; \
	else \
	    echo "WARNING: In a virtualenv, do not try to update user's pipenv and pip"; \
	fi

pipenv-install-dev:
	@$(pipenv --venv)
	# Do not use destructive "--python" or "--three" option if the venv already exists
	# See https://github.com/pypa/pipenv/issues/349
	@if [ $$? -eq 0 ]; then \
		echo "$(PIPENV) install --dev $(PIPENV_LOCK_ARGS)" ; \
		$(PIPENV) install --dev $(PIPENV_LOCK_ARGS) ; \
	else \
		echo "$(PIPENV) install --dev $(PIPENV_LOCK_ARGS) --python $(PYTHON)" ; \
		$(PIPENV) install --dev $(PIPENV_LOCK_ARGS) --python $(PYTHON) ; \
	fi
	pipenv run pip install -e .


mk-venv: clean-venv
	mkdir -p .venv

.venv: mk-venv

clean-venv:
	@rm -rf .venv

install-local: install-local-only-deps install-local-only-curpackage

install-local-only-deps:
	# Install only dependencies
	$(PIPENV) install --deploy {%- if not cookiecutter.is_application %} --skip-lock {%- endif %}

install-local-only-curpackage:
	# Install current package as well
	$(PIPENV) run pip install .

pipenv-install-anyway:
	if [ -f Pipfile.lock ]; then \
		pipenv install --dev --ignore-pipfile; \
	else \
		pipenv install --dev --skip-lock; \
	fi;
	pipenv run pip install -e .

pipenv-install-inspect:
	pipenv install --skip-lock --dev
	pipenv graph


# ==================================================================================================
# Code formatting targets
# ==================================================================================================

style: isort autopep8 yapf  ## Format code

isort:
	$(PIPENV) run isort -y -rc $(MODULES)

autopep8:
	$(PIPENV) run autopep8 --in-place --recursive setup.py $(MODULES)

yapf:
	$(PIPENV) run yapf --style .yapf --recursive -i $(MODULES)

format: style


# ==================================================================================================
# Static checks targets
# ==================================================================================================

checks: pep508 isort-check yapf-check flake8 pylint mypy bandit pydocstyle  ## Static analysis

pep508:
	$(PIPENV) check

isort-check:
	$(PIPENV) run isort -c -rc $(MODULES)

yapf-check:
	pipenv run yapf --style .yapf --recursive --diff $(MODULES)

flake8:
	$(PIPENV) run python setup.py flake8

pylint:
	$(PIPENV) run pylint --rcfile=.pylintrc --output-format=colorized $(MODULES)

mypy:
	# Static type checker only enabled on methods that uses Python Type Annotations
	$(PIPENV) run mypy --config-file .mypy.ini $(MODULES)

bandit:
	pipenv run bandit -c .bandit.yml -r $(MODULES)

pydocstyle:
	pipenv run pydocstyle $(MODULES)

clean-mypy:
	rm -rf .mypy_cache || true

sc: style check

sct: style check test


# ==================================================================================================
# Test targets
# ==================================================================================================

test:  ## Execute unit tests
	$(PIPENV) run pytest $(MODULES)

test-v:
	$(PIPENV) run pytest -vv $(MODULES)

test-coverage:
	$(PIPENV) run py.test -v --cov $(PACKAGE_NAME) --cov-report html:coverage_html --cov-report term $(MODULES)


# ==================================================================================================
# Distribution packages targets
# ==================================================================================================

dists: requirements sdist wheels  ## Build all distribution packages

build: dists

sdist:
	$(PIPENV) run python setup.py sdist

wheel:
	$(PIPENV) run python setup.py bdist_wheel

clean-dist:
	rm -rfv build dist/


{% if cookiecutter.docker_build == 'y' -%}

# ==================================================================================================
# Docker targets
# ==================================================================================================

docker:   ## Build docker image
	docker build .


{% endif %}
# ==================================================================================================
# Misc targets
# ==================================================================================================

shell:
	$(PIPENV) shell

ctags:
	find -name '*.py' -exec ctags -a {} \;

update: clean-pipenv ensure-pipenv mk-venv pipenv-update pipenv-install-dev requirements  ## Update dependencies

pipenv-update:
	$(PIPENV) update --clear
	mkdir -p .venv

requirements:
	# A "requirements.txt" is needed when pip installing your module until PBR supports `Pipfile`
	$(PIPENV) run pipenv_to_requirements
	{% if cookiecutter.is_application -%}
	# Also freeze requirements from lock file for applications, for information purpose
	$(PIPENV) run pipenv_to_requirements --freeze --output requirements-prod.txt
	{%- endif %}

update-recreate: update style check test

lock:
	$(PIPENV) lock --clear


githook: style requirements


# ==================================================================================================
# Publish targets
# ==================================================================================================

tag-pbr:  ## Print commands to tag next release
	@{ \
		set -e ;\
		export VERSION=$$($(PIPENV) run python setup.py --version | cut -d. -f1,2,3); \
		echo "I: Computed new version: $$VERSION"; \
		echo "I: presse ENTER to accept or type new version number:"; \
		read VERSION_OVERRIDE; \
		VERSION=$${VERSION_OVERRIDE:-$$VERSION}; \
		PROJECTNAME=$$($(PIPENV) run python setup.py --name); \
		echo "I: Tagging $$PROJECTNAME in version $$VERSION with tag: $$VERSION" ; \
		echo "$$ git tag -s $$VERSION -m \"$$PROJECTNAME $$VERSION\""; \
		echo "I: Pushing tag $$VERSION, press ENTER to continue, C-c to interrupt"; \
		read _; \
		echo "$$ git push origin $$VERSION"; \
	}
	@# Note:
	@# To sign, need gpg configured and the following command:
	@#  git tag -s $$VERSION -m \"$$PROJECTNAME $$VERSION\""

push: githook
	git push origin --all
	git push origin --tags

publish: clean-dist dists
	$(PIPENV) run python setup.py sdist bdist_wheel upload -r pypi-test || true


# ==================================================================================================
# Clean targets
# ==================================================================================================

clean: clean-dist clean-docs clean-mypy clean-venv clean-pipenv   ## Clean environment
	find . -name '__pycache__'  -exec rm -rf {} \; || true
	find . -name '.cache'  -exec rm -rf {} \; || true
	find . -name '*.egg-info'  -exec rm -rf {} \; || true
	find . -name "*.pyc" -exec rm -f {} \; || true
	rm -rf .pytest_cache || true
	rm -rf coverage_html || true

clean-pipenv:
	$(PIPENV) --rm || true

# ==================================================================================================
# Documentation targets
# ==================================================================================================

DOCS_EXCLUSION=$(foreach m, $(MODULES), $m/tests)

docs: clean-docs sdist docs-generate-apidoc docs-run-sphinx  ## Build online documentation

docs-generate-apidoc:
	pipenv run sphinx-apidoc \
		--force \
		--separate \
		--module-first \
		--doc-project "API Reference" \
		-o docs/source/reference \
		$(PACKAGE_NAME) \
			$(DOCS_EXCLUSION)

docs-run-sphinx:
	pipenv run make -C docs/ html

clean-docs:
	rm -rf docs/_build docs/source/reference/*.rst

docs-open:
	xdg-open docs/_build/html/index.html


# ==================================================================================================
# Run targets
# ==================================================================================================

run:
	# add you run commands here
	$(PIPENV) run $(EXECUTABLE_NAME)


# ==================================================================================================
# Aliases to gracefully handle typos on poor dev's terminal
# ==================================================================================================

check: checks
devel: dev
develop: dev
dist: dists
doc: docs
styles: style
test-unit: test
tests: test
unit-tests: test
unittest: test
unittests: test
ut: test
wheels: wheel
