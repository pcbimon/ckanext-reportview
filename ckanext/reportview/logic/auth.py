import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def reportview_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "reportview_get_sum": reportview_get_sum,
    }
