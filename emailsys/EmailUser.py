import uuid

class User:
    def __init__(self, email, password):
        self.id = uuid.uuid4()
        self.email = email
        self.password = password
        self.mailbox = {
            'default': {
                'sent': [],
                'received': [],
                'spam': []
            },
            'user_folders': {}
        }
        self.blocked_senders = set()

    def __str__(self):
        return (f"User ID: {self.id}\n"
                f"Email: {self.email}\n"
                f"Sent Emails: {len(self.mailbox['default']['sent'])}\n"
                f"Received Emails: {len(self.mailbox['default']['received'])}\n"
                f"Spam Emails: {len(self.mailbox['default']['spam'])}")
    
