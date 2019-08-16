# SMPT Email Sender
import smtplib

import secret
# Config and Content
MY_ADDRESS = secret.ADDRESS
USERNAME = secret.USERNAME
PASSWORD = secret.PASSWORD
HOST = secret.HOST
PORT = secret.PORT
RECIEVER_ADDRESS = secret.RECIEVER_ADDRESS
SUBJECT = secret.SUBJECT
CONTENT = secret.CONTENT


def main():

    # set up the SMTP server
    s = smtplib.SMTP(host=HOST)  # Add as parameter if required by mail server: port=PORT
    s.starttls()
    s.ehlo()
    s.login(USERNAME, PASSWORD)

    # For each contact, send the email:
    BODY = '\r\n'.join(['To: %s' % RECIEVER_ADDRESS,
                        'From: %s' % MY_ADDRESS,
                        'Subject: %s' % SUBJECT,
                        '', CONTENT])

    try:
        s.sendmail(MY_ADDRESS, [RECIEVER_ADDRESS], BODY)
        print('email sent')
    except:
        print('error sending mail')

    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == '__main__':
    main()
