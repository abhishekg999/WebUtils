"""
JSCore contains helpers and functions exported from pythonmonkey.
All JSNative functions are prefixed with js_.
"""

from pythonmonkey import eval as js_eval
from pythonmonkey import require as js_require
from pythonmonkey import undefined as js_undefined
import pythonmonkey 

js_encodeURIComponent = pythonmonkey.encodeURIComponent

js_he = js_require('he')
def he_encode(text, options=None):
    return js_he.encode(text, options)

