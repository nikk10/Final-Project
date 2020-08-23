#! /usr/bin/env python3

#print statements provide additional debugging as needed

#for PDF
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
#formatting PDF
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import date


def generate_report(attachment, title, paragraph):
    #print(fruits)
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles["h1"])
    #print(report_title)
    report_body = Paragraph(paragraph, styles["BodyText"])
    report.build([report_title, report_body])
