"""Tests for views.py."""

import pytest

import ckanext.reportview.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "reportview")
@pytest.mark.usefixtures("with_plugins")
def test_reportview_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("reportview.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, reportview!"
