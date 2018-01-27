"""PytSite Tumblr Plugin API Functions.
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import reg as _reg
from . import _error


def get_app_key() -> str:
    """Get application's key.
    """
    app_key = _reg.get('tumblr.app_key') or _reg.get('tumblr.app_key')

    if not app_key:
        raise _error.AppKeyNotSet("Configuration parameter 'tumblr.app_key' is not set")

    return app_key


def get_app_secret() -> str:
    """Get application's secret key.
    """
    app_secret = _reg.get('tumblr.app_secret') or _reg.get('tumblr.app_secret')

    if not app_secret:
        raise _error.AppSecretNotSet("Configuration parameter 'tumblr.app_secret' is not set")

    return app_secret
