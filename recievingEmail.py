import imaplib
import getpass
import email

M = imaplib.IMAP4_SSL("imap.gmail.com")
emailadd = input("Email: ")
password = getpass.getpass("Password: ")
M.login(emailadd, password)

M.select("INBOX")
typ, data = M.search(None, 'SUBJECT "REPLACE WITH SUBJECT!!!"')

email_id = data[0]
result, email_data = M.fetch(email_id, "(RFC822)")

raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

email_msg = email.message_from_string(raw_email_string)

for part in email_msg.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)

