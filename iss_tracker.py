import requests
import logging

logger = logging.getLogger(__name__)
ISS_NOW_URL = "http://api.open-notify.org/iss-now.json"

def get_iss_location():
    try:
        r = requests.get(ISS_NOW_URL, timeout=10)
        r.raise_for_status()
        data = r.json()
        pos = data.get("iss_position", {})
        return {"latitude": pos.get("latitude"), "longitude": pos.get("longitude")}
    except Exception:
        return None
