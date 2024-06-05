import uuid
import datetime

class Email:
    def __init__(self, sender, recipient, subject, body, tags):
        self.id = uuid.uuid4()
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.tags = tags
        self.date = datetime.datetime.now()

    def __str__(self):
        return (f"Email ID: {self.id}\n"
                f"From: {self.sender}\n"
                f"To: {self.recipient}\n"
                f"Subject: {self.subject}\n"
                f"Date: {self.date}\n"
                f"Tags: {', '.join(self.tags)}\n"
                f"Body:\n{self.body}")
    
    