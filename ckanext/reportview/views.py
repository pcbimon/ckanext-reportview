from flask import Blueprint


reportview = Blueprint(
    "reportview", __name__)


def page():
    return "Hello, reportview!"


reportview.add_url_rule(
    "/reportview/page", view_func=page)


def get_blueprints():
    return [reportview]
