import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "230500226mycput@gmail.com"
    smtp_password = "example123"
    
    sender_email = "230500226mycput@gmail.com"
    receiver_email = "230500226@mycput.ac.za"
    subject = "Test Email"
    body = "This is a test email sent from Python."

    # Create a MIMEText object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(smtp_user, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        server.quit()
        print("SMTP server connection closed")

if __name__ == "__main__":
    send_email()
