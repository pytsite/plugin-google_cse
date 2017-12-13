"""PytSite Google Custom Search Plugin Event Handlers
"""
from pytsite import tpl as _tpl, lang as _lang, router as _router, reg as _reg
from plugins import assetman as _assetman, auth as _auth

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    """'pytsite.router.dispatch' handler.
    """
    cx = _reg.get('google_cse.cx')
    if not cx and _auth.get_current_user().has_permission('google_cse.settings.manage'):
        _router.session().add_warning_message(_lang.t('google_cse@plugin_setup_required_warning'))
    else:
        _assetman.add_inline(_tpl.render('google_cse@js', {'cx': cx}))