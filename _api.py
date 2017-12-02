"""PytSite Google Custom Search API
"""
from pytsite import reg as _reg
from . import _error

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def get_cx():
    cx = _reg.get('google_cse.cx')

    if not cx:
        raise _error.SearchEngineIdNotDefined()

    return cx
