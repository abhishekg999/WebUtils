import random
import string


ALPHANUMERIC = string.ascii_letters + string.digits
def random_string(n):
    return ''.join(random.choice(ALPHANUMERIC) for _ in range(n))