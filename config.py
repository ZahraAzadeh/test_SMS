import os
import logging

# -------------------------
# Email Settings
# -------------------------

EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# -------------------------
# SMTP compatibility (for send_email.py)
# -------------------------

SMTP_HOST = EMAIL_HOST
SMTP_PORT = EMAIL_PORT
SMTP_USER = EMAIL_ADDRESS
SMTP_PASS = EMAIL_PASSWORD

EMAIL_FROM = EMAIL_ADDRESS
EMAIL_TO = os.getenv("EMAIL_TO")

# -------------------------
# Logging
# -------------------------

LOG_FILE = os.getenv("LOG_FILE", "app.log")
LOG_LEVEL_NAME = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_LEVEL = getattr(logging, LOG_LEVEL_NAME, logging.INFO)

# -------------------------
# SMS / MeliPayamak Settings
# -------------------------

MELI_API_KEY = os.getenv("MELIPAYAMAK_API_KEY")
SMS_SENDER = os.getenv("SMS_SENDER")
SMS_RECEIVER = os.getenv("SMS_RECEIVER")
