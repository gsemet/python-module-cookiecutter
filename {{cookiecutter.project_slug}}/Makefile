.PHONY: build docs

# ==================================================================================================
# Variables
# ==================================================================================================

MODULE:={{ cookiecutter.project_slug }}


# ==================================================================================================
# do-it-all targets
# ==================================================================================================

all: dev style checks dists test

dev: ensure-pipenv pipenv-install-dev requirements ln-venv


# ==================================================================================================
# Install targets
# ==================================================================================================

ensure-pipenv:
	pip3 install --user --upgrade 'pipenv>=9.0' 'pip>=9.0'
	@echo "ensure your local python install is in your PATH"

pipenv-install-dev:
	pipenv install --dev

ln-venv:
	# use that to configure a symbolic link to the virtualenv in .venv
	rm -rf .venv
	ln -s $$(pipenv --venv) .venv

.venv: ln-venv

install-local: install-local-only-deps install-local-only-curpackage

install-local-only-deps:
	# Install only dependencies
	pipenv install

install-local-only-curpackage:
	# Install current package as well
	pipenv run pip install .


# ==================================================================================================
# Code formatting targets
# ==================================================================================================

style: isort autopep8 yapf

isort:
	pipenv run isort -y -rc $(MODULE)

autopep8:
	pipenv run autopep8 --in-place --recursive setup.py $(MODULE)

yapf:
	pipenv run yapf --style .yapf --recursive -i $(MODULE)

format: style


# ==================================================================================================
# Static checks targets
# ==================================================================================================

checks: pep508 isort-check flake8 pylint mypy

pep508:
	pipenv check

isort-check:
	pipenv run isort -c -rc $(MODULE)

flake8:
	pipenv run python setup.py flake8

pylint:
	pipenv run pylint --rcfile=.pylintrc --output-format=colorized $(MODULE)

mypy:
	# Static type checker only enabled on methods that uses Python Type Annotations
	pipenv run mypy --config-file .mypy.ini $(MODULE)

clean-mypy:
	rm -rf .venv .mypy_cache || true

sc: style check

sct: style check test

# ==================================================================================================
# Test targets
# ==================================================================================================

test:
	pipenv run pytest $(MODULE)

test-v:
	pipenv run pytest -vv $(MODULE)

test-coverage:
	pipenv run py.test -v --cov $(MODULE) --cov-report term-missing


# ==================================================================================================
# Distribution packages targets
# ==================================================================================================

dists: requirements sdist bdist wheels

build: dists

sdist:
	pipenv run python setup.py sdist

bdist:
	pipenv run python setup.py bdist

wheel:
	pipenv run python setup.py bdist_wheel

clean-dist:
	rm -rfv build dist/


{%- if cookiecutter.docker_build %}
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
	pipenv shell

ctags:
	find -name '*.py' -exec ctags -a {} \;

update: pipenv-update dev

pipenv-update:
	pipenv update

requirements:
	# needed until PBR supports `Pipfile`
	{% if cookiecutter.is_application -%}
	# Freeze requirements for applications
	pipenv run pipenv_to_requirements --freeze
	{% else -%}
	pipenv run pipenv_to_requirements
	{%- endif %}

update-recreate: update style check test

lock:
	pipenv lock


githook: style requirements


# ==================================================================================================
# Publish targets
# ==================================================================================================

tag-pbr:
	@{ \
		set -e ;\
		export VERSION=$$(pipenv run python setup.py --version | cut -d. -f1,2,3); \
		echo "I: Computed new version: $$VERSION"; \
		echo "I: presse ENTER to accept or type new version number:"; \
		read VERSION_OVERRIDE; \
		VERSION=$${VERSION_OVERRIDE:-$$VERSION}; \
		PROJECTNAME=$$(pipenv run python setup.py --name); \
		echo "I: Tagging $$PROJECTNAME in version $$VERSION with tag: $$VERSION" ; \
		echo "$$ git tag $$VERSION -m \"$$PROJECTNAME $$VERSION\""; \
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
	pipenv run python setup.py sdist bdist_wheel upload -r nexus || true



# ==================================================================================================
# Clean targets
# ==================================================================================================

clean: clean-dist clean-docs clean-mypy
	pipenv --rm || true
	find . -name '__pycache__'  -exec rm -rf {} \; || true
	find . -name '.cache'  -exec rm -rf {} \; || true
	find . -name '*.egg-info'  -exec rm -rf {} \; || true
	find . -name "*.pyc" -exec rm -f {} \; || true


# ==================================================================================================
# Documentation targets
# ==================================================================================================

docs: clean-docs sdist
	pipenv run make -C docs/ html

clean-docs:
	rm -rfv docs/_build

docs-apidoc:
	pipenv run sphinx-apidoc \
		-f \
		-o docs/source/reference \
		-e \
		--no-toc \
		--no-headings \
		{{ cookiecutter.project_slug }} \
			{{ cookiecutter.project_slug }}/tests

docs-open:
	xdg-open docs/_build/html/index.html


# ==================================================================================================
# Run targets
# ==================================================================================================

run:
	# add you run commands here
	# pipenv run ...


# ==================================================================================================
# Aliases to gracefully handle typos on poor dev's terminal
# ==================================================================================================

check: checks
devel: dev
develop: dev
doc: docs
dist: dists
styles: style
test-unit: test
unittest: test
unittests: test
unit-tests: test
ut: test
wheels: wheel
