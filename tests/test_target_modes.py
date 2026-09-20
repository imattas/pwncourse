import os

import pytest


def test_target_configuration_defaults_local(monkeypatch):
    monkeypatch.delenv("PWN_REMOTE", raising=False)
    monkeypatch.delenv("PWN_HOST", raising=False)
    monkeypatch.delenv("PWN_PORT", raising=False)
    from labs.common.target import target_configuration

    assert target_configuration() == {"mode": "local"}


def test_remote_configuration_requires_host_and_port(monkeypatch):
    monkeypatch.setenv("PWN_REMOTE", "1")
    monkeypatch.delenv("PWN_HOST", raising=False)
    monkeypatch.setenv("PWN_PORT", "31337")
    from labs.common.target import target_configuration

    assert target_configuration() == {"mode": "remote", "host": "127.0.0.1", "port": 31337}


def test_remote_configuration_rejects_missing_port(monkeypatch):
    monkeypatch.setenv("PWN_REMOTE", "1")
    monkeypatch.delenv("PWN_HOST", raising=False)
    monkeypatch.delenv("PWN_PORT", raising=False)
    from labs.common.target import target_configuration

    with pytest.raises(ValueError, match="PWN_PORT"):
        target_configuration()
