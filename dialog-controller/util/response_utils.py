# encoding: utf-8
import json

from flask import Response


def make_response(data, status_code):
    """Returns HTTP response for a request

    Args:
        data: JSON with response information
        status_code: status code for HTTP response

    Returns:
        HTTP response
    """

    json_data = json.dumps(data)
    return Response(response=json_data, status=status_code, mimetype='application/json')

def make_error_response(status_code):
    """Returns HTTP error response with default JSON for a request

    Args:
        status_code: status code for HTTP response

    Returns:
        HTTP response
    """

    answer = {}
    answer["answer"] = {}
    answer["answer"]["next"] = ""
    answer["answer"]["question"] = []

    entry = {}
    entry["id"] = -2
    entry["transcript"] = "No entendí correctamente. ¿Puede repetir la pregunta?"
    entry["type"] = ""
    answer["answer"]["question"].append(entry)

    answer["answer"]["session"] = ""

    return make_response(answer, status_code)
