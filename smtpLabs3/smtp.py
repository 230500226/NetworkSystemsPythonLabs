import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    # SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "230500226mycput@gmail.com"
    smtp_password = "REDACTED"

    # Email details
    sender_email = "230500226mycput@gmail.com"
    receiver_email = "230500226@mycput.ac.za"
    subject = "Test Email 230500226"
    body = "This is a test email sent from Python 230500226 numbder 3."

    # Create a MIMEText object to represent the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(smtp_user, smtp_password)  # Log in to the SMTP server
        
        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        # Handle SMTP-related errors
        print(f"Failed to send email: {e}")

    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")

    finally:
        # Close the connection to the SMTP server
        server.quit()
        print("SMTP server connection closed")

if __name__ == "__main__":
    send_email()
