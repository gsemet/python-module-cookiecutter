# coding: utf-8

import logging


log = logging.getLogger(__name__)


class MyPublicClass():
    def run(self) -> int:
        print("Hello World")
        return 0


    def load_data(self):
        import importlib_resources
        import {{cookiecutter.project_slug}}.data
        # Store and load data from within the module using new importlib_resources
        # See https://importlib-resources.readthedocs.io/en/latest/using.html#example
        with importlib_resources.path({{cookiecutter.project_slug}}.data,
                                      'data.json') as s:
            print("filename: ", s)
