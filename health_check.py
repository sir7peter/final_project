"""
Created on Sun Nov 03 15:16:00 2023

@author: pedro

Script that will run in the background monitoring some of the system statistics:
CPU usage, disk space, available memory and name resolution.
Moreover, this Python script should send an email if there are problems, such as:

Report an error if CPU usage is over 80%
Report an error if available disk space is lower than 20%
Report an error if available memory is less than 100MB
Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
"""
#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails

def stats(argv):
    if psutil.cpu_percent() > 80:
        flag = print('Error - CPU usage is over 80%')
    elif (shutil.disk_usage('/').free / shutil.disk_usage('/').total) < 20:
        flag = print('Error - Available disk space is less than 20%')
    elif (psutil.virtual_memory().available / 1024**2) < 100:
        flag = print('Error - Available memory is less than 100MB')
    elif socket.gethostname('localhost') != '127.0.0.1':
        flag = print('Error - localhost cannot be resolved to 127.0.0.1')
    return flag

def main(argv):
    email_param = {'sender': 'automation@example.com'
        , 'recipient': 'student@example.com'
        , 'subject': stats()
        , 'body': 'Please check your system and resolve the issue as soon as possible.'}

    if email_param['subject']:
        try:
            message = emails.generate_email(email_param['sender'], email_param['recipient'], email_param['subject']
                          ,email_param['body'])
            emails.send_email(message)
        except:
            print('Unable to send meesage')
    else:
        print('System is good.')

if __name__ == '__main__':
    main()