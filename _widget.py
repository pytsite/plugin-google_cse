"""PytSite Google Custom Search Plugin Widgets

See https://developers.google.com/custom-search/docs/element for details.
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import html as _html
from plugins import widget as _widget
from . import _api


class Search(_widget.Abstract):
    """
    """

    def __init__(self, uid: str, **kwargs):
        super().__init__(uid, **kwargs)

        self._form_group = False
        self._has_messages = False
        self._js_modules.append('google-cse-widget')
        self._link_target = kwargs.get('link_target', '_self')
        self._enable_order_by = kwargs.get('enable_order_by', False)
        self._data['cx'] = kwargs.get('cx', _api.get_cx())

    def _get_element(self) -> _html.Element:
        return _html.Div(
            uid=self._uid,
            css='gcse-search',
            data_linkTarget=self._link_target,
            data_enableOrderBy='true' if self._enable_order_by else 'false',
        )


class SearchBoxOnly(Search):
    def _get_element(self) -> _html.Element:
        return _html.Div(uid=self._uid, css='gcse-searchbox-only')


class SearchResultsOnly(Search):
    def _get_element(self) -> _html.Element:
        return _html.Div(
            uid=self._uid,
            css='gcse-searchresults-only',
            data_linkTarget=self._link_target,
            data_enableOrderBy='true' if self._enable_order_by else 'false',
        )
