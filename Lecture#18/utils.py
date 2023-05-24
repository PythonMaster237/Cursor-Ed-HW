from flask import abort

def get_or_404_custom(data):
    if data is None:
        return abort(404)
