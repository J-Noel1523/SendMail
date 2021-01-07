# make sure to get email access keys from your Gmail
import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()

email = input("Email Please: ")
password = getpass.getpass("Password Please: ")
smtp_object.login(email, password)

from_address = email
to_address = input("Recipient's email: ")
subject = input("Subject Line: ")
message = input("Write message: ")
msg = f'Subject: {subject}\n\n{message}\netc'
#msg = 'Subject: {}\n\n{}'.format(subject, message)
smtp_object.sendmail(from_address, to_address, msg)
smtp_object.quit()