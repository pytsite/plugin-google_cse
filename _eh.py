"""PytSite Google Custom Search Plugin Event Handlers
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import tpl, lang, router, reg
from plugins import assetman, auth


def router_dispatch():
    """'pytsite.router.dispatch' handler.
    """
    cx = reg.get('google_cse.cx')
    if not cx and auth.get_current_user().has_role('dev'):
        router.session().add_warning_message(lang.t('google_cse@plugin_setup_required_warning'))
    else:
        assetman.inline_js(tpl.render('google_cse@js', {'cx': cx}))
