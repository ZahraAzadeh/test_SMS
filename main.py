import logging, logging.handlers
from config import LOG_FILE, LOG_LEVEL
from iss_tracker import get_iss_location
from send_sms import send_sms
from send_email import send_email
logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)
fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=2_000_000, backupCount=3)
fh.setFormatter(fmt)
logger.addHandler(fh)

def run_once():
    loc = get_iss_location()
    if not loc:
        send_email("ISS error", "Failed to fetch location")
        return
    msg = f"ISS at lat {loc['latitude']}, lon {loc['longitude']}"
    r = send_sms(msg)
    if not r.get("ok"):
        send_email("SMS failed", str(r))

if __name__ == "__main__":
    run_once()
