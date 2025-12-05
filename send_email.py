import smtplib
from email.message import EmailMessage
import logging
from config import (
    SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS,
    EMAIL_FROM, EMAIL_TO
)

logger = logging.getLogger(__name__)


def send_email(subject: str, body: str, to_address: str = None) -> bool:
    """
    Send an email using SMTP server.

    Args:
        subject (str): Email subject.
        body (str): Email plain text content.
        to_address (str, optional): Destination email. Falls back to EMAIL_TO.

    Returns:
        bool: True if sent successfully, False otherwise.
    """

    to_addr = to_address or EMAIL_TO
    if not to_addr:
        logger.error("No destination email address provided.")
        return False

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_FROM
    msg["To"] = to_addr
    msg.set_content(body)

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=20) as smtp:
            smtp.starttls()
            smtp.login(SMTP_USER, SMTP_PASS)
            smtp.send_message(msg)

        logger.info(f"Email sent successfully to {to_addr}")
        return True

    except Exception as e:
        logger.error(f"Failed to send email to {to_addr}: {e}")
        return False
