from urllib.parse import quote as _quote
from urllib.parse import unquote as _unquote

def encodeURIComponent(uriComponent):
    return _quote(uriComponent, safe="!'()*")


def encodeURIComponentAll(uriComponent):
    return _quote(uriComponent, safe="")


def decodeURIComponent(encodedURI):
    return _unquote(encodedURI)
