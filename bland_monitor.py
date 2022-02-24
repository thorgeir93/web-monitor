"""
Run with python3.5
"""
from monitor import Crawler

class BlandCrawler(Crawler):
    def extract_id(self, tag, attrs):
        """
        """
        attrs = dict(attrs)
        _id = attrs.get('href', '').split('/')
        _id = list(filter(None, _id))
        return _id.pop()
    
    def harvest_html(self, tag, attrs):
        if not tag == 'a':
            return
        
        attrs = dict(attrs)

        title = attrs.get('title')
        if not title:
            return

        return title.strip()

    def monitor_get_link(self, tag, attrs): 
        attrs = dict(attrs)
        return 'http://bland.is{0}'.format(attrs.get('href'))


def main():
    crawler = BlandCrawler( **sofi )
    crawler.start()

    crawler.std_out_result()

    

sofi = {
    'keys': ( ['sófi', 'sofi'], ),
    'url': (
        'https://bland.is/solutorg/'
        'heimilid/stofa-sofi/?categoryId=29'
    ),
    "work_dir": "/home/thorgeir/data"
}

hjol = {
    'keys': (
        ['hjól', 'hjol'],
    ),
    'url': (
        'https://bland.is/solutorg/'
        'ithrottir-heilsa/reidhjol/?categoryId=88'
    ),
    "work_dir": "/home/thorgeir/data/"
}


import smtplib

sender = 'thorgeir@megas'
receivers = ['thorgeirsigurd@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <thorgeirsigurd@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except Exception as error:
   print(error)
   print("Error: unable to send email")
1/0

import smtplib, ssl

smtp_server = "localhost"
port = 465  # For starttls
sender_email = "localhost"
receiver_email = "thorgeirsigurd@gmail.com"
#password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    #server.login(sender_email, password)
    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, "hallo")

    #message = """\
    #Subject: Hi there

    #This message is sent from Python."""

    #with smtplib.SMTP(smtp_server, port, context=context) as server:
    #    #server.login(sender_email, password)
    #    server.sendmail(sender_email, receiver_email, message)

except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 
