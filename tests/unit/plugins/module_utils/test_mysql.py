from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from unittest.mock import MagicMock

from ansible_collections.ansible.mysql.plugins.module_utils.mysql import get_server_version, get_server_implementation
from ..utils import dummy_cursor_class


@pytest.mark.parametrize(
    'cursor_return_version,cursor_return_type',
    [
        ('5.7.0-mysql', 'dict'),
        ('8.0.0-mysql', 'list'),
        ('10.5.0-mariadb', 'dict'),
        ('10.5.1-mariadb', 'list'),
    ]
)
def test_get_server_version(cursor_return_version, cursor_return_type):
    """
    Test that server versions are handled properly by get_server_version() whether they're returned as a list or dict.
    """
    cursor = dummy_cursor_class(cursor_return_version, cursor_return_type)
    assert get_server_version(cursor) == cursor_return_version


@pytest.mark.parametrize(
    'cursor_return_version,cursor_return_type,server_implementation',
    [
        ('5.7.0-mysql', 'dict', 'mysql'),
        ('8.0.0-mysql', 'list', 'mysql'),
        ('10.5.0-mariadb', 'dict', 'mariadb'),
        ('10.5.1-mariadb', 'list', 'mariadb'),
    ]
)
def test_get_server_implementation(cursor_return_version, cursor_return_type, server_implementation):
    """
    Test that server implementation are handled properly by get_server_implementation() whether the server version returned as a list or dict.
    """
    module = MagicMock()
    cursor = dummy_cursor_class(cursor_return_version, cursor_return_type)

    assert get_server_implementation(module, cursor) == server_implementation


def test_get_server_implementation_warns_on_mariadb():
    """Test that a deprecation warning is emitted when MariaDB is detected."""
    module = MagicMock()
    cursor = dummy_cursor_class('10.5.0-mariadb', 'dict')

    get_server_implementation(module, cursor)

    module.warn.assert_called_once()
    assert 'MariaDB has been detected' in module.warn.call_args[0][0]
    assert '6.0.0' in module.warn.call_args[0][0]
    assert 'ansible.mariadb' in module.warn.call_args[0][0]


def test_get_server_implementation_no_warning_on_mysql():
    """Test that no warning is emitted when MySQL is detected."""
    module = MagicMock()
    cursor = dummy_cursor_class('8.0.0-mysql', 'dict')

    get_server_implementation(module, cursor)

    module.warn.assert_not_called()
