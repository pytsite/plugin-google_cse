"""PytSite Google Custom Search Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import plugman as _plugman

if _plugman.is_installed(__name__):
    # Public API
    from . import _widget as widget


def _register_assetman_resources():
    from plugins import assetman

    if not assetman.is_package_registered(__name__):
        assetman.register_package(__name__)
        assetman.js_module('google-cse-widget', __name__ + '@js/google-cse-widget')
        assetman.t_js(__name__)

    return assetman


def plugin_install():
    _register_assetman_resources().build(__name__)


def plugin_load():
    _register_assetman_resources()


def plugin_load_uwsgi():
    from pytsite import lang, tpl, router
    from plugins import permissions, settings
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__)
    tpl.register_package(__name__)

    # Lang globals
    lang.register_global('google_cse_admin_settings_url',
                         lambda language, args: settings.form_url('google_cse'))

    # Permissions
    permissions.define_permission('google_cse.settings.manage', 'google_cse@manage_google_cse_settings', 'app')

    # Settings
    settings.define('google_cse', _settings_form.Form, 'google_cse@google_cse', 'fa fa-search',
                    'google_cse.settings.manage')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)
