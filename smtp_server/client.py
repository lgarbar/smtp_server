import smtplib
from email import message_from_file
import logging

logging.basicConfig(level=logging.DEBUG)

def send_eml_file(path_to_eml):
    try:
        with open(path_to_eml, 'r') as file:
            msg = message_from_file(file)
        server = smtplib.SMTP('127.0.0.1', 25)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        logging.info("Email sent successfully.")
    except FileNotFoundError:
        logging.error(f"The file {path_to_eml} was not found.")
    except smtplib.SMTPException as e:
        logging.error(f"SMTP error occurred: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

path_to_eml = "/Users/danielgarcia-barnett/Desktop/smtp/disney_email/Your Disney Store order is on its way!.eml"
send_eml_file(path_to_eml)