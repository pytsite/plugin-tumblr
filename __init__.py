"""PytSite Tumblr Plugin.
"""
# Public API
from ._session import AuthSession, Session

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import lang, assetman, permissions, settings, events
    from . import _content_export, _settings_form, _eh

    # Resources
    lang.register_package(__name__, alias='tumblr')
    assetman.register_package(__name__, alias='tumblr')

    # Lang globals
    lang.register_global('tumblr_admin_settings_url', lambda: settings.form_url('tumblr'))

    # Content export driver
    try:
        from plugins import content_export
        content_export.register_driver(_content_export.Driver())
    except ImportError as e:
        raise RuntimeError("Required plugin is not found: {}".format(e))

    # Permissions
    permissions.define_permission('tumblr.settings.manage', 'tumblr@manage_tumblr_settings', 'app')

    # Settings
    settings.define('tumblr', _settings_form.Form, 'tumblr@tumblr', 'fa fa-tumblr', 'tumblr.settings.manage')

    # Event handlers
    events.listen('pytsite.router.dispatch', _eh.router_dispatch)


_init()
