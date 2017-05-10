"""PytSite Google Custom Search Plugin
"""
from . import _widget as widget

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import lang, tpl, permissions, settings, router, assetman
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__, alias='google_cse')
    tpl.register_package(__name__, alias='google_cse')

    assetman.register_package(__name__, alias='google_cse')
    assetman.js_module('google-cse-widget', __name__ + '@js/google-cse-widget')
    assetman.t_js(__name__ + '@**')

    # Lang globals
    lang.register_global('google_cse_admin_settings_url',
                         lambda language, args: settings.form_url('google_cse'))

    # Permissions
    permissions.define_permission('google_cse.settings.manage',
                                  'google_cse@manage_google_cse_settings', 'app')

    # Settings
    settings.define('google_cse', _settings_form.Form, 'google_cse@google_cse',
                    'fa fa-search', 'google_cse.settings.manage')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)


_init()
