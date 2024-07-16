"""Tests for helpers.py."""

import ckanext.reportview.helpers as helpers


def test_reportview_hello():
    assert helpers.reportview_hello() == "Hello, reportview!"
