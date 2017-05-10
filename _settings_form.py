"""PytSite Google Custom Search Plugin Settings Form.
"""
from pytsite import widget as _widget, lang as _lang, settings as _settings, validation as _validation

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Form(_settings.Form):
    def _on_setup_widgets(self):
        self.add_widget(_widget.input.Text(
            uid='setting_cx',
            weight=10,
            label=_lang.t('google_cse@search_engine_id'),
            required=True,
            help=_lang.t('google_cse@search_engine_id_setup_help'),
            rules=_validation.rule.Regex(pattern='^\d+:[a-z0-9]+$')
        ))

        super()._on_setup_widgets()
