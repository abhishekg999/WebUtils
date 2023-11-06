HTTP_BASE_URL = None

def setHTTPBaseURL(url: str):
    global HTTP_BASE_URL
    # assert valid blah blah
    HTTP_BASE_URL = url.rstrip('/')

__all__ = ["HTTPSync", "HTTPAsync", "HTTPEncodings", "Utils", "JSCore", "Utils"]