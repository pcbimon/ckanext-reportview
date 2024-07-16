
def reportview_hello():
    return "Hello, reportview!"


def get_helpers():
    return {
        "reportview_hello": reportview_hello,
    }
