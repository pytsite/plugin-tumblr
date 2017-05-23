"""PytSite Tumblr Plugin.
"""
# Public API
from ._api import get_app_key, get_app_secret
from . import _session as session, _widget as widget

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import lang, permissions, settings, router
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__, alias='tumblr')

    # Lang globals
    lang.register_global('tumblr_admin_settings_url', lambda language, args: settings.form_url('tumblr'))

    # Permissions
    permissions.define_permission('tumblr.settings.manage', 'tumblr@manage_tumblr_settings', 'app')

    # Settings
    settings.define('tumblr', _settings_form.Form, 'tumblr@tumblr', 'fa fa-tumblr', 'tumblr.settings.manage')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)


_init()
