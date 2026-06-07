# SMTP Email Sender

Small educational project demonstrating:

- SMTP authentication
- MIME messages
- File attachments
- Base64 encoding

## Requirements

- Python 3.11+
- SMTP server
- Two Fake or Temporary Email accounts

## Usage

python mail.py

## Concepts

### SMTP:
- Service that carries the message

### MIME (Multipurpose Internet Mail Extensions)
- It defines how the message is structured.

### MIMEText: 
- Part of the message that contains the text (No mandatory)
- Example:

``` Python
msg.attach(MIMEText(message, 'plain'))
```
It implicitly generates the following content:
```
Content-Type: text/plain

Hola, este es mi mensaje.
```

### MIMEBase
- Generic class to represent any MIME content
- Example:
``` Python
p = MIMEBase('application', 'octet-stream')
```
It means:
- application: app data
- octet-stream: arbitrary sequence of bytes (to attach files)
```
Content-Type: application/octet-stream
```

### MIMEMultipart
- The email is divided into several parts; Multipart acts as a container to group all these parts
- Example:
``` Python
msg = MIMEMultipart()
msg.attach(MIMEText(...))
msg.attach(image)
msg.attach(pdf)
```
