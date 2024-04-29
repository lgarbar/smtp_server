import asyncore
from smtpd import SMTPServer
from email.parser import Parser
from email.utils import formatdate
import os

class EMLReceiver(SMTPServer):
    SENDER_NAME = "Etsy Transactions"
    SENDER_EMAIL = "transaction@etsy.com"

    def __init__(self, localaddr, remoteaddr):
        super().__init__(localaddr, remoteaddr)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.mbox_filename = os.path.join(script_dir, "..", "received_email.mbox")
        self.message_number = 0
    
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        msg_data = data.decode('utf-8')  # Decode bytes to string
        date_time = "Thu, 09 Nov 2023 07:14:33 -0700"
        
        # Set the sender information
        sender_info = f"From {self.SENDER_NAME} <{self.SENDER_EMAIL}> {date_time}\n"
        
        with open(self.mbox_filename, "a") as mbox_file:
            mbox_file.write(sender_info)  # Set the sender information
            mbox_file.write(msg_data)
            mbox_file.write("\n")  # Message separator
        
        print("Email received and saved as", self.mbox_filename)
        self.message_number += 1

def run_server():
    server = EMLReceiver(('127.0.0.1', 1025), None)
    print("SMTP Server listening on port 1025...")
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print("SMTP Server stopped.")

if __name__ == "__main__":
    run_server()
