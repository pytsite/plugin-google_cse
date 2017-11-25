"""PytSite Google Custom Search API
"""
from plugins import settings as _settings
from . import _error

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def get_cx():
    cx = _settings.get('google_cse.cx')

    if not cx:
        raise _error.SearchEngineIdNotDefined()

    return cx
