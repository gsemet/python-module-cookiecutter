.PHONY: build docs

# ==================================================================================================
# Variables
# ==================================================================================================

MODULES:={{ cookiecutter.project_slug }}
PACKAGE_NAME:={{ cookiecutter.project_slug }}
PIP:=/usr/bin/env python3 -m pip
PIPENV:=pipenv
PYTHON:=python3


# ==================================================================================================
# do-it-all targets
# ==================================================================================================

all: dev style checks dists test

dev: clean-ln-venv ensure-pipenv pipenv-install-dev requirements ln-venv


# ==================================================================================================
# Install targets
# ==================================================================================================

ensure-pipenv:
	$(PIP) install --user --upgrade 'pipenv>=11.10.1' 'pip>=10'
	@echo "ensure your local python install is in your PATH"

pipenv-install-dev:
	$(PIPENV) install --dev {%- if not cookiecutter.is_application %} --skip-lock {%- endif %} --python $(PYTHON)
	$(PIPENV) run pip install -e .

ln-venv: clean-ln-venv
	# use that to configure a symbolic link to the virtualenv in .venv
	ln -s $$($(PIPENV) --venv) .venv

.venv: ln-venv

clean-ln-venv:
	@rm -f .venv

install-local: install-local-only-deps install-local-only-curpackage

install-local-only-deps:
	# Install only dependencies
	$(PIPENV) install --deploy {%- if not cookiecutter.is_application %} --skip-lock {%- endif %}

install-local-only-curpackage:
	# Install current package as well
	$(PIPENV) run pip install .


# ==================================================================================================
# Code formatting targets
# ==================================================================================================

style: isort autopep8 yapf

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

checks: pep508 isort-check yapf-check flake8 pylint mypy bandit pydocstyle

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

test:
	$(PIPENV) run pytest $(MODULES)

test-v:
	$(PIPENV) run pytest -vv $(MODULES)

test-coverage:
	$(PIPENV) run py.test -v --cov $(PACKAGE_NAME) --cov-report html:coverage_html --cov-report term $(MODULES)


# ==================================================================================================
# Distribution packages targets
# ==================================================================================================

dists: requirements sdist bdist wheels

build: dists

sdist:
	$(PIPENV) run python setup.py sdist

bdist:
	$(PIPENV) run python setup.py bdist

wheel:
	$(PIPENV) run python setup.py bdist_wheel

clean-dist:
	rm -rfv build dist/


{%- if cookiecutter.docker_build == 'y' %}


# ==================================================================================================
# Docker targets
# ==================================================================================================

docker:
	docker build .


{%- endif %}


# ==================================================================================================
# Misc targets
# ==================================================================================================

shell:
	$(PIPENV) shell

ctags:
	find -name '*.py' -exec ctags -a {} \;

update: pipenv-update dev

pipenv-update:
	$(PIPENV) update

requirements:
	# needed until PBR supports `Pipfile`
	{% if cookiecutter.is_application -%}
	# Freeze requirements for applications
	$(PIPENV) run pipenv_to_requirements --freeze
	{% else -%}
	$(PIPENV) run pipenv_to_requirements
	{%- endif %}

update-recreate: update style check test

lock:
	$(PIPENV) lock


githook: style requirements


# ==================================================================================================
# Publish targets
# ==================================================================================================

tag-pbr:
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

clean: clean-dist clean-docs clean-mypy clean-ln-venv
	$(PIPENV) --rm || true
	find . -name '__pycache__'  -exec rm -rf {} \; || true
	find . -name '.cache'  -exec rm -rf {} \; || true
	find . -name '*.egg-info'  -exec rm -rf {} \; || true
	find . -name "*.pyc" -exec rm -f {} \; || true
	rm -rf .pytest_cache || true
	{% if not cookiecutter.is_application -%}
	rm -rf Pipfile.lock || true
	{%- endif %}


# ==================================================================================================
# Documentation targets
# ==================================================================================================

DOCS_EXCLUSION=$(foreach m, $(MODULES), $m/tests)

docs: clean-docs sdist docs-generate-apidoc docs-run-sphinx

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
	$(PIPENV) run {{ cookiecutter.project_slug }}


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
