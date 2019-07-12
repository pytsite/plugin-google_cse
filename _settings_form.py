"""PytSite Google Custom Search Plugin Settings Form.
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang, validation
from plugins import widget, settings


class Form(settings.Form):
    def _on_setup_widgets(self):
        self.add_widget(widget.input.Text(
            uid='setting_cx',
            weight=10,
            label=lang.t('google_cse@search_engine_id'),
            required=True,
            help=lang.t('google_cse@search_engine_id_setup_help'),
            rules=validation.rule.Regex(pattern='^\d+:[a-z0-9]+$')
        ))

        super()._on_setup_widgets()
