#!/usr/bin/env python3

from email.message import EmailMessage
import os.path
import mimetypes
import smtplib
import getpass


def generate_email(sender, recipient, subject, body, attachment_path):
    message = EmailMessage()
    #sender = "sender@example.com"
    #recipient = "recipient@example.com"
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)
    #attachment_path = "~/Pictures/flower.jpeg"
    if attachment_path != "":
        attachment_filename = os.path.basename(attachment_path)
        print(os.path.basename(attachment_path))
        #to send an attachment, you need to get the mimetype and mime subtype
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split("/",1)
        with open(attachment_path, "rb") as ap:
            message.add_attachment(ap.read(),
            maintype = mime_type,
            subtype = mime_subtype,
            filename =os.path.basename(attachment_path))
    return message

def send_email(message):
    mail_server = smtplib.SMTP_SSL("smtp.example.com")
    #unsure if next two lines needed
    mail_server.set_debuglevel(1)
    #mail_pass = getpass.getpass("Password? ")
    #will probably be able to send emails without login
    #mail_server.login(sender, mail_pass)
    mail_server.send_message(message)
    mail_server.quit()
