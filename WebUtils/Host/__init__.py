from WebUtils.Encodings import encodeURIComponent

__all__ = ["https_host"]

HTTP_HOST_URL = "http://reflect-html.glitch.me/#"
HTTPS_HOST_URL = "https://reflect-html.glitch.me/#"

def https_host(src : str) -> str:
    """
    Takes an HTML source string, returns it hosted on a page with HTTPS enabled.
    Hosts page on https://reflect-html.glitch.me/.
    Returns url of hosted page.
    """

    html = encodeURIComponent(src)
    return f"{HTTPS_HOST_URL}{html}"

def http_host(src : str) -> str:
    """
    Takes an HTML source string, returns it hosted on a page with HTTPS enabled.
    Hosts page on https://reflect-html.glitch.me/.
    Returns url of hosted page.
    """
    html = encodeURIComponent(src)
    return f"{HTTP_HOST_URL}{html}"