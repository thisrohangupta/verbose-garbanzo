import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path):
    # Set up the email parameters
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Attach the file to the email
    filename = attachment_path.split("/")[-1]
    attachment = open(attachment_path, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")
    message.attach(part)

    # Connect to the email server and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Change the server and port if using a different provider
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Command-line arguments
    parser = argparse.ArgumentParser(description="Send an email with an attachment.")
    parser.add_argument("sender_email", help="Your email address")
    parser.add_argument("sender_password", help="Your email password or app password")
    parser.add_argument("receiver_email", help="Recipient's email address")
    parser.add_argument("subject", help="Email subject")
    parser.add_argument("body", help="Email body")
    parser.add_argument("attachment_path", help="Path to the file you want to attach")
    args = parser.parse_args()

    # Call the function with command-line arguments
    send_email(args.sender_email, args.sender_password, args.receiver_email,
               args.subject, args.body, args.attachment_path)
