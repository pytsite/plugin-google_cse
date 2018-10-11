"""PytSite Google Custom Search Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from . import _widget as widget


def plugin_load_wsgi():
    from pytsite import lang, router
    from plugins import settings
    from . import _settings_form, _eh

    # Lang globals
    lang.register_global('google_cse_admin_settings_url', lambda language, args: settings.form_url('google_cse'))

    # Settings
    settings.define('google_cse', _settings_form.Form, 'google_cse@google_cse', 'fa fa-search', 'dev')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)
