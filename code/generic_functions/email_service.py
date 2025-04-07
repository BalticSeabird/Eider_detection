import smtplib
from email.message import EmailMessage
from datetime import datetime

# Get time
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Email details
sender_email = "jhsemailservice@gmail.com"
app_password = input("Please type gmail password ... ")  # 16-character app password
recipient_email = "jonas.sundberg@slu.se"
subject = f"Run of EJDER1 on GPU 1 completed {now} !"
body = "No body, just a test email."

# Create the email
msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject
msg.set_content(body)


# Send the email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender_email, app_password)
    smtp.send_message(msg)

print("Email on finished run sent successfully!")
