import getpass
import smtplib

HOST = "smtp.gmail.com"
PORT = 587

FROM_EMAIL = "samplexmail@gmail.com"
TO_EMAIL = "Samimsekhlinux@gmail.com"

PASSWORD = "iuzvfdojkpojcewt"

MESSAGE = """gude_gondho_nai

Keyword arguments:
argument --gud gud gud
Return: return_description
"""

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)

smtp.quit()