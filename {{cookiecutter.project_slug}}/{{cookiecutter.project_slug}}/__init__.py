# coding: utf-8

import pbr.version


def version():
    return pbr.version.VersionInfo('{{ cookiecutter.project_slug }}').release_string()


# __version__ = version()
#
#
# __all__ = [
#     '__version__',
# ]
