import sendgrid
import os
from sendgrid.helpers.mail import *

sg = SendGridAPIClient(
    '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')
from_email = Email("test@example.com")
to_email = To("test@example.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
