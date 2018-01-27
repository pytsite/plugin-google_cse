"""PytSite Google Custom Search Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from . import _widget as widget


def plugin_load():
    from plugins import assetman

    assetman.register_package(__name__)
    assetman.js_module('google-cse-widget', __name__ + '@js/google-cse-widget')
    assetman.t_js(__name__)


def plugin_install():
    from plugins import assetman

    assetman.build(__name__)


def plugin_load_uwsgi():
    from pytsite import lang, tpl, router
    from plugins import settings
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__)
    tpl.register_package(__name__)

    # Lang globals
    lang.register_global('google_cse_admin_settings_url', lambda language, args: settings.form_url('google_cse'))

    # Settings
    settings.define('google_cse', _settings_form.Form, 'google_cse@google_cse', 'fa fa-search', 'dev')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)
