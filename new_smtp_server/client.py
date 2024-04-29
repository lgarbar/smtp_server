import smtplib
from email.message import EmailMessage

def send_email():
    msg = EmailMessage()
    msg.set_content("Test email content")

    msg['Subject'] = "Test Subject"
    msg['From'] = "sender@example.com"
    msg['To'] = "receiver@example.com"

    # Load the .eml file content
    with open("/Users/danielgarcia-barnett/Desktop/smtp/etsy_email/Your Etsy Purchase from hicrethobby (3280854413).eml", 'rb') as eml_file:
        eml_content = eml_file.read()
    
    # Send the .eml content as an email
    try:
        with smtplib.SMTP('localhost', 1025) as server:
            server.sendmail(msg['From'], msg['To'], eml_content)
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    send_email()
