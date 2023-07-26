# Email Python Script

## Introduction

Here is a python script to send emails, it takes in the argument of:

1. **Your_Email:** This is your email that you went to use to send the message from
2. **Your_Email_Password:** Provide a token for the script to use to send an email on your behalf, you can use the harness expression `<+secret.getValue("account.emailToken")>
3. **Recipient Email:** Who are you going to send the email to, this could be a user group email address or a non-harness user email address
4. **Subject**: The fourth argument is the subject of the email that you want to send
5. **Body**: The fifth argument is the message body you want to send
6. **Attachment**: The sixth argument is the attachment you want to send

### Sample Usage

```BASH
python send_email.py your_email@gmail.com your_email_password recipient@example.com "Test Email with Attachment" "This is a test email with an attachment. Please check the attached file." path_to_your_file.pdf
```
