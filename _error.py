"""PytSite Google Custom Search Plugin Errors
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class SearchEngineIdNotDefined(RuntimeError):
    def __str__(self):
        return "Setting 'google_cse.cx' is not defined"
