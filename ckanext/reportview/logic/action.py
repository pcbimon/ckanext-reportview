import ckan.plugins.toolkit as tk
import ckanext.reportview.logic.schema as schema


@tk.side_effect_free
def reportview_get_sum(context, data_dict):
    tk.check_access(
        "reportview_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.reportview_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'reportview_get_sum': reportview_get_sum,
    }
