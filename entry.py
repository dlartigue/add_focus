import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
from config import FROM_EMAIL, EMAIL_PASS, OMNIFOCUS_EMAIL


class New_Entry():

    def __init__(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)

    def create(self, title, note):
        '''
        Create email object with a subject and a body.
        '''
        self.entry = MIMEMultipart()
        self.entry['To'] = OMNIFOCUS_EMAIL
        self.entry['From'] = FROM_EMAIL
        self.entry['Subject'] = title
        self.entry.attach(MIMEText(note, 'plain'))
        self.entry = self.entry.as_string()

    def send(self):
        '''
        Send email object to the omnifocus maildrop address.
        '''
        self.server.starttls()
        self.server.login(FROM_EMAIL, EMAIL_PASS)
        self.server.sendmail(FROM_EMAIL, OMNIFOCUS_EMAIL, self.entry)
        self.server.quit()


def quick_add(single_line_item):
    '''
    Quickly add an entry with a single string formatted as 'title; note'.
    '''
    try:
        entry_parts = re.split(';', single_line_item)
        quick_entry = New_Entry()
        if len(entry_parts) == 2:
            quick_entry.create(entry_parts[0], entry_parts[1])
        else:
            quick_entry.create(entry_parts[0], '')
        quick_entry.send()
        print('\nSent to OmniFocus!')
    except:
        print('Something happened...')
