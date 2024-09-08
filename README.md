# Python Email Automation Script

## Overview

This Python script automates the process of sending emails to multiple recipients using Gmail's SMTP server. The script can be customized to send personalized messages by modifying the email content, subject, and recipients list.

## Features

- Uses Gmail's SMTP server to send emails.
- Sends the same email to multiple recipients in a loop.
- Handles potential errors and ensures the server connection is closed properly.

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.x**: This script requires Python 3.x to run. You can download and install Python from the official website: [https://www.python.org/](https://www.python.org/).

2. **smtplib Library**: The `smtplib` and `email.mime` libraries are part of Python's standard library, so you don't need to install any additional packages.

3. **Gmail Account**: You need a Gmail account to send the emails. If your account has two-factor authentication (2FA) enabled, you will need to generate an **App-Specific Password**. You can do that by following [Google's guide](https://support.google.com/accounts/answer/185833).

## Setup

1. **Update Email Credentials:**
   - Replace `email1@gmail.com` with your own Gmail address.
   - Replace `abcde` with your Gmail password or app-specific password if 2FA is enabled.

2. **Update Recipient List:**
   - Modify the `receiver_emails` list to include the email addresses you want to send the email to.

3. **Update Email Content:**
   - Update the `subject` variable to customize the subject of the email.
   - Update the `body` variable to change the content of the email.

## Code Explanation

- **Imports**: 
  - `email.mime.multipart` and `email.mime.text` are used to structure and format the email.
  - `smtplib` is used to establish an SMTP connection and send the email.

- **Server Setup**: 
  - Connects to Gmail's SMTP server (`smtp.gmail.com`) on port 587.
  - Starts the connection in TLS mode for security.
  - Logs in using the sender's Gmail credentials.

- **Email Sending**: 
  - For each recipient in the `receiver_emails` list, a new email is created with the specified subject and body.
  - The email is then sent to the recipient using the `sendmail` function.

- **Error Handling**: 
  - If any error occurs during the process, it is caught and printed.
  
- **Closing the Connection**: 
  - Ensures that the SMTP server connection is properly closed in the `finally` block.

## How to Run

1. Clone or download the script.
2. Open a terminal/command prompt and navigate to the directory where the script is located.
3. Run the script using the following command:
   ```bash
   python email_automation.py
   ```

## Notes

- **Security**: Do not hard-code sensitive credentials in the script. It is recommended to store passwords in environment variables or use a credentials manager.
- **Gmail Limits**: Gmail has limitations on the number of emails you can send per day. Be mindful of these limits to avoid having your account temporarily locked.

## License

This project is licensed under GNU General Public License v3.0.

