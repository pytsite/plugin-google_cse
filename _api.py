"""PytSite Google Custom Search API
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import reg
from . import _error


def get_cx():
    cx = reg.get('google_cse.cx')

    if not cx:
        raise _error.SearchEngineIdNotDefined()

    return cx
