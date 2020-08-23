#! /usr/bin/env python3

import os
from datetime import date

import json
import reports
import emails

#print statements provide additional debugging as needed

#state file locations for the json input and the pdf attachment
#state sender and recipient email addresses
json_location = ""
attachment= ""
sender = ""
recipient = ""

#print(date.today())


if __name__ == "__main__":
    with open(json_location) as json_file:
        fruits = json.load(json_file)
        #print(fruits)
        title = "Processed Update on {}".format(date.today())
        paragraph = ""
        fruit_list = []
        for fruit in fruits:
            #print(fruit)
            fruit_list.append("")
            fruit_list.append("name: " + fruit["name"])
            fruit_list.append("weight: " + str(fruit["weight"])+" lbs")
        print(fruit_list)
        paragraph="<br/>".join(fruit_list)
        print(paragraph)
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website sucessfully. A detailed list is attached to this email."
    reports.generate_report(attachment, title, paragraph)
    message = emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email(message)
