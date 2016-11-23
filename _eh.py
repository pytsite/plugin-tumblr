"""PytSite Tumblr Plugin Event Handlers.
"""
from pytsite import settings as _settings, auth as _auth, lang as _lang, router as _router

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    """'pytsite.router.dispatch' event handler.
    """
    if _auth.get_current_user().has_permission('tumblr.settings.manage'):
        msg = _lang.t('tumblr@plugin_setup_required_warning')
        if not _settings.get('tumblr.app_key') or not _settings.get('tumblr.app_secret'):
            _router.session().add_warning_message(msg)
        else:
            _router.session().get_warning_message(msg)
