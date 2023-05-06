import smtplib
from email.message import EmailMessage



# we asked the user to input his email
sender = input("Enter the email of the sender: ")

# we made the recipient a loop that will continue to run until the user types "done"
recipient_list = []
while True:
    recipient = input("Enter the email address of recipient (type 'done' to finish): ")
    if recipient.lower() == 'done':
        break
    recipient_list.append(recipient)

# we asked the user to input password,subject and content
mypassword = input("Enter your password: ")
subject = input("Enter the subject of the mail: ")
content = input("What is your content: ")

# we called the objects of the class Emailmessage
email_msg = EmailMessage()
email_msg['Subject'] = subject
email_msg['From'] = sender
email_msg['To'] = ', '.join(recipient_list)
email_msg.set_content(content)

# we used smtp to send the message
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender,mypassword)
    smtp.send_message(email_msg)
    print('email sent')