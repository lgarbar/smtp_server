from smtpd import SMTPServer
import asyncore
import logging

logging.basicConfig(level=logging.DEBUG)

class CustomSMTPServer(SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        logging.info(f"Processing message from {mailfrom} to {rcpttos}")
        try:
            with open('received_email.mbox', 'ab') as mbox_file:
                mbox_file.write(b"From \n")  # Add mbox delimiter
                mbox_file.write(data + b"\n\n")
            logging.info("Message written to mbox file successfully.")
        except Exception as e:
            logging.error(f"Failed to write to mbox file: {e}")

def run_smtp_server():
    server = CustomSMTPServer(('127.0.0.1', 25), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        logging.info("Server shutdown requested by user.")
        server.close()
    finally:
        asyncore.close_all()

if __name__ == "__main__":
    run_smtp_server()