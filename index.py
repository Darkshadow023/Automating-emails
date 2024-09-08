from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

sender_email = "email1@gmail.com"  # change this to your own email
password = "abcde"  # use an app-specific password if 2FA is enabled

# List of recipient email addresses
receiver_emails = ["example1@gmail.com", "example2@gmail.com", "example3@gmail.com"]

subject = "Hello from python email automation"
body = "This is an automated email sent using Python."

# Set up the server connection
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)

    # Create the email
    for receiver_email in receiver_emails:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Attach the body as plain text
        message.attach(MIMEText(body, "plain"))

        # Send the email to each recipient
        server.sendmail(sender_email, receiver_email, message.as_string())
        print(f"Email sent to {receiver_email} successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    server.quit()
