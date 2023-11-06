"""
Literally just grequests with a_ prefix.
"""
import grequests
from grequests import map as a_map
from grequests import imap as a_imap
from grequests import imap_enumerated as a_imap_enumerated

a_get = grequests.get
a_options = grequests.options 
a_head = grequests.head 
a_post = grequests.post 
a_put = grequests.put 
a_patch = grequests.patch
a_delete = grequests.delete 