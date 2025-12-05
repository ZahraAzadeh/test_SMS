import time
from config import HTTP_RETRIES, HTTP_BACKOFF_SECONDS

def retry(func):
    last = None
    for a in range(1, HTTP_RETRIES+1):
        try: return func()
        except Exception as e:
            last = e
            time.sleep(HTTP_BACKOFF_SECONDS * a)
    raise last
