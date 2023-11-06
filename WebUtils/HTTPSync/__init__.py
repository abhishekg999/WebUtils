import WebUtils
import requests

def get(url: str, params=None, **kwargs):
    if url.startswith('/') and WebUtils.HTTP_BASE_URL:
        url = WebUtils.HTTP_BASE_URL + url
        
    response = requests.get(url, params, **kwargs)
    return response

def post(url: str, data=None, json=None, **kwargs):
    if url.startswith('/') and WebUtils.HTTP_BASE_URL:
        url = WebUtils.HTTP_BASE_URL + url

    response = requests.post(url, data, json, **kwargs)
    return response



