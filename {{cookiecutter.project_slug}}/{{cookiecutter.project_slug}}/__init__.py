# coding: utf-8

import pbr.version

import {{ cookiecutter.project_slug }}._{{ cookiecutter.project_slug }} import MyPublicClass


def version():
    return pbr.version.VersionInfo('{{ cookiecutter.project_slug }}').release_string()

## Uncomment the following line to declare a __version__ in your root module. Beware the evaluation
## of the version may impact the load time of your module
#
# __version__ = version()
#
#
__all__ = [
#     '__version__',
    'MyPublicClass',
]
