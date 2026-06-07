import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.server.com'
port = 465 # 25 = SMTP, 465 = SSL, 587 = TLS
sender = 'sender1234@email.com'
receiver = 'receiver1234@email.com'

# Create connection
server = smtplib.SMTP(smtp_server, port) 

# Start a secure connection (465 or 587) 
server.starttls()

# Start a simple connection (25)
#server.ehlo() 

# Read password from a file (avoiding plain text)
with open('password.txt', 'r') as f:
    password = f.read().strip() # strip avoids any \n at the end 

# If there's an error with authentication 
try:
    server.login(sender, password)
except smtplib.SMTPAuthenticationError:
    print("Authentication failed")

msg = MIMEMultipart()
msg['From'] = 'USER_NAME'
msg['To'] = receiver
msg['subject'] = 'Subject of the email'

with open('messageMail.txt', 'r') as f:
    message = f.read()

#Load message
msg.attach(MIMEText(message), 'plain') #(text, Type: plain text)

filename = 'image.png'

p = MIMEBase('application', 'octet-stream')

# When attachment finishes, it closes
with open(filename, 'rb') as attachment: # rb = read in byte mode (to open it as an image)
    p.set_payload(attachment.read())

# Code image as base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', f'attachment; filename={filename}')

msg.attach(p)

text = msg.as_string()
server.sendmail(sender, receiver, text)

# Close SMTP connection
server.quit()