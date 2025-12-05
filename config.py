import os

# -------------------------
# SMS / MeliPayamak Settings
# -------------------------

MELI_API_KEY = os.getenv("MELIPAYAMAK_API_KEY")  # Your API key (token)
SMS_SENDER = os.getenv("SMS_SENDER")             # Your Melipayamak line number
SMS_RECEIVER = os.getenv("SMS_RECEIVER")         # Destination phone

# -------------------------
# Email Settings
# -------------------------

EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# -------------------------
# ISS Tracking Settings
# -------------------------

ISS_CHECK_INTERVAL = int(os.getenv("ISS_CHECK_INTERVAL", "60"))
ALERT_DISTANCE_KM = int(os.getenv("ALERT_DISTANCE_KM", "2000"))

# -------------------------
# Logging
# -------------------------

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# -------------------------
# HTTP Retry Settings
# -------------------------

HTTP_RETRIES = int(os.getenv("HTTP_RETRIES", "3"))
HTTP_BACKOFF_SECONDS = int(os.getenv("HTTP_BACKOFF_SECONDS", "2"))
