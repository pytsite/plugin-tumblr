"""PytSite Tumblr Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import plugman as _plugman

if _plugman.is_installed(__name__):
    # Public API
    from ._api import get_app_key, get_app_secret
    from . import _session as session, _widget as widget


def plugin_load():
    from pytsite import lang, router
    from plugins import permissions, settings
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__)

    # Lang globals
    lang.register_global('tumblr_admin_settings_url', lambda language, args: settings.form_url('tumblr'))

    # Permissions
    permissions.define_permission('tumblr.settings.manage', 'tumblr@manage_tumblr_settings', 'app')

    # Settings
    settings.define('tumblr', _settings_form.Form, 'tumblr@tumblr', 'fa fa-tumblr', 'tumblr.settings.manage')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)
