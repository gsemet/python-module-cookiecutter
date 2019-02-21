# coding: utf-8

import logging

# {{ cookiecutter.project_name }} Modules
from {{cookiecutter.project_slug}}._{{cookiecutter.project_slug}} import MyPublicClass

log = logging.getLogger(__name__)


def main() -> int:
    return MyPublicClass().run()

if __name__ == '__main__':
    sys.exit(main())
