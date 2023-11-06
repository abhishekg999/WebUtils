from pythonmonkey import eval as js_eval
from pythonmonkey import require as js_require
from pythonmonkey import undefined as js_undefined
import pythonmonkey 

encodeURIComponent = pythonmonkey.encodeURIComponent

_he = js_require('he')
def he_encode(text, options=None):
    return _he.encode(text, options)

