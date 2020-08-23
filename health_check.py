#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails

def email_alert(subject):
    sender = "automation@example.com"
    recipient = "user@example.com"
    body = "Please check your system and resolve the issue as soon as possible."
    attachment_path = ""
    message = emails.generate_email(sender, recipient, subject, body, attachment_path)
    emails.send_email(message)

if __name__ == "__main__":
    if psutil.cpu_percent() > 0.8:
        email_alert("Error: CPU usage is over 80%")
    total, used, free = shutil.disk_usage("/")
    percent_free_disk = free/total
    if percent_free_disk < 0.2
        email_alert("Error: Available disk space is less than 20%")
    threshold = 500*1024*1024
    if psutil.virtual_memory().available < threshold:
        email_alert("Available memory is less than 500 MB")
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    if ip_address != "127.0.0.1":
        email_alert("Error: localhost cannot be resolved to 127.0.0.1")
