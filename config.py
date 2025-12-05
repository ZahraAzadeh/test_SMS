import os
import logging

# -------------------------
# Helper: Check required env vars
# -------------------------
def get_env_var(name: str, required=True):
    value = os.getenv(name)
    if required and not value:
        raise ValueError(f"Environment variable '{name}' is not set")
    return value

# -------------------------
# SMS / Melipayamak Settings
# -------------------------
MELI_API_KEY = get_env_var("MELIPAYAMAK_API_KEY")
SMS_SENDER = get_env_var("SMS_SENDER")
SMS_RECEIVER = get_env_var("SMS_RECEIVER")

# -------------------------
# Email Settings
# -------------------------
EMAIL_ADDRESS = get_env_var("EMAIL_ADDRESS")
EMAIL_PASSWORD = get_env_var("EMAIL_PASSWORD")

# SMTP compatibility for send_email.py
SMTP_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("EMAIL_PORT", "587"))
SMTP_USER = EMAIL_ADDRESS
SMTP_PASS = EMAIL_PASSWORD
EMAIL_FROM = EMAIL_ADDRESS
EMAIL_TO = os.getenv("EMAIL_TO", EMAIL_ADDRESS)  # default to self if not set

# -------------------------
# Logging
# -------------------------
# مسیر لاگ: اگر LOG_FILE ست نشده باشد، از logs/app.log استفاده می‌کند
LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")

# ایجاد پوشه لاگ در صورت عدم وجود
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# LOG_LEVEL: تبدیل از string به logging constant
LOG_LEVEL_NAME = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_LEVEL = getattr(logging, LOG_LEVEL_NAME, logging.INFO)

# -------------------------
# ISS Tracking Settings
# -------------------------
ISS_CHECK_INTERVAL = int(os.getenv("ISS_CHECK_INTERVAL", "60"))
ALERT_DISTANCE_KM = int(os.getenv("ALERT_DISTANCE_KM", "2000"))

# -------------------------
# HTTP Retry Settings
# -------------------------
HTTP_RETRIES = int(os.getenv("HTTP_RETRIES", "3"))
HTTP_BACKOFF_SECONDS = int(os.getenv("HTTP_BACKOFF_SECONDS", "2"))
