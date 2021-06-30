#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 22:28:49 2019

@author: caiyizhao
"""

import smtplib
from email.mime.text import MIMEText

# sender info：email address，QQ email mailbox authorization code
from_addr = input('Please enter your email address：')
password = '-'

# receiver email info
to_addr = []
while True:
    a=input('Please enter whom you are sending this email to：')
    to_addr.append(a)
    b=input('Need to enter other email address."n" to quit，press any other key to continue')
    if b=='n':
        break


# server
smtp_server = 'smtp.qq.com'


# email content
msg = MIMEText('''Hi! How are you today?''','plain','utf-8')

from email.header import Header
msg['From:']=Header(from_addr)
msg['To:']=Header(to_addr)
msg['Subject:']=Header('Greetings')

# turn on the server
server = smtplib.SMTP_SSL('smtp.qq.com')
server.connect(smtp_server,465)
# log in email
server.login(from_addr, password)
# send the email
server.sendmail(from_addr, to_addr, msg.as_string())
# turn off the server
server.quit()