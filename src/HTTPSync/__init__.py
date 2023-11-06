import requests

def get(url, params=None, **kwargs):
    response = requests.get(url, params, kwargs)
    return response

def post(url, data=None, json=None, **kwargs):
    response = requests.post(url, data, json, kwargs)
    return response



