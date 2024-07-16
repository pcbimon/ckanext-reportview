"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.reportview.logic import validators


def test_reportview_reauired_with_valid_value():
    assert validators.reportview_required("value") == "value"


def test_reportview_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.reportview_required(None)
