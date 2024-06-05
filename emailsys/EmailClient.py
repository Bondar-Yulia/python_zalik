from emailsys.EmailSystem import EmailSystem
from emailsys.Email import Email

class EmailClient(EmailSystem):
    def send_email(self, sender_email, recipient_email, subject, body, tags):
        if sender_email not in self.users or recipient_email not in self.users:
            print("Sender or recipient email does not exist.")
            return
        email = Email(sender_email, recipient_email, subject, body, tags)
        self.add_email(email, sender_email, 'sent')
        
        if self.classify_as_spam(recipient_email, email):
            self.add_email(email, recipient_email, 'spam')
        else:
            self.add_email(email, recipient_email, 'received')

    def create_folder(self, user_email, folder_name):
        if user_email not in self.users:
            print(f"User with email {user_email} does not exist.")
            return
        user = self.users[user_email]
        if folder_name in user.mailbox['default'] or folder_name in user.mailbox['user_folders']:
            print(f"Folder {folder_name} already exists.")
            return
        user.mailbox['user_folders'][folder_name] = []
        print(f"Folder {folder_name} created successfully.")

    def clear_folder(self, user_email, folder_name):
        if user_email not in self.users:
            print(f"User with email {user_email} does not exist.")
            return
        user = self.users[user_email]
        if folder_name in user.mailbox['default']:
            user.mailbox['default'][folder_name] = []
            print(f"Default folder {folder_name} cleared.")
        elif folder_name in user.mailbox['user_folders']:
            user.mailbox['user_folders'][folder_name] = []
            print(f"User folder {folder_name} cleared.")
        else:
            print(f"Folder {folder_name} does not exist.")

    def delete_folder(self, user_email, folder_name):
        if user_email not in self.users:
            print(f"User with email {user_email} does not exist.")
            return
        user = self.users[user_email]
        if folder_name in user.mailbox['default']:
            print(f"Cannot delete default folder {folder_name}.")
            return
        if folder_name not in user.mailbox['user_folders']:
            print(f"Folder {folder_name} does not exist.")
            return
        del user.mailbox['user_folders'][folder_name]
        print(f"Folder {folder_name} deleted successfully.")

    def classify_as_spam(self, user_email, email):
        if user_email not in self.users:
            print(f"User with email {user_email} does not exist.")
            return
        user = self.users[user_email]
        spam_keywords = ["win", "free", "prize", "click here", "urgent"]
        if any(keyword in email.subject.lower() or keyword in email.body.lower() for keyword in spam_keywords):
            return True
        if email.sender in user.blocked_senders:
            return True
        return False

    def block_sender(self, user_email, sender_email):
        if user_email not in self.users:
            print(f"User with email {user_email} does not exist.")
            return
        user = self.users[user_email]
        user.blocked_senders.add(sender_email)
        print(f"Sender {sender_email} added to blocked list.")
