from emailsys.EmailUser import User
from emailsys.Email import Email
from emailsys.EmailSystemBase import EmailSystemBase

class EmailSystem(EmailSystemBase):
    def __init__(self):
        self.users = {}

    def add_user(self, email, password):
        if email in self.users:
            print(f"User with email {email} already exists.")
            return
        user = User(email, password)
        self.users[email] = user
        print(f"User {email} added successfully.")

    def delete_user(self, email):
        if email not in self.users:
            print(f"User with email {email} does not exist.")
            return
        del self.users[email]
        print(f"User {email} deleted successfully.")

    def add_email(self, email, user_email, folder_name='received'):
        if user_email not in self.users:
            print(f"User with email {user_email} does not exist.")
            return

        user = self.users[user_email]

        if folder_name in user.mailbox['default']:
            user.mailbox['default'][folder_name].append(email)
        else:
            if folder_name not in user.mailbox['user_folders']:
                user.mailbox['user_folders'][folder_name] = []
            user.mailbox['user_folders'][folder_name].append(email)

        print(f"Email added to {folder_name} folder of {user_email}.")

    def delete_email(self, user_email, email_id):
        if user_email not in self.users:
            print(f"User with email {user_email} does not exist.")
            return

        user = self.users[user_email]

        def remove_email_from_folder(folder):
            for email in folder:
                if email.id == email_id:
                    folder.remove(email)
                    return True
            return False
        
        for folder in user.mailbox['default'].values():
            if remove_email_from_folder(folder):
                print(f"Email {email_id} deleted from {user_email}'s mailbox.")
                return

        for folder in user.mailbox['user_folders'].values():
            if remove_email_from_folder(folder):
                print(f"Email {email_id} deleted from {user_email}'s mailbox.")
                return

        print(f"Email {email_id} not found in {user_email}'s mailbox.")

    def search_emails(self, user_email, **kwargs):
        if user_email not in self.users:
            print(f"User with email {user_email} does not exist.")
            return []

        emails = self.users[user_email].mailbox['default']['received'] + self.users[user_email].mailbox['default']['sent']
        for folder in self.users[user_email].mailbox['user_folders'].values():
            emails.extend(folder)

        if 'subject' in kwargs:
            emails = [email for email in emails if kwargs['subject'].lower() in email.subject.lower()]

        if 'tags' in kwargs:
            emails = [email for email in emails if any(tag in email.tags for tag in kwargs['tags'])]

        if 'date_from' in kwargs and 'date_to' in kwargs:
            emails = [email for email in emails if kwargs['date_from'] <= email.date <= kwargs['date_to']]

        if 'sender' in kwargs:
            emails = [email for email in emails if kwargs['sender'].lower() in email.sender.lower()]

        if 'recipient' in kwargs:
            emails = [email for email in emails if kwargs['recipient'].lower() in email.recipient.lower()]

        return emails

    def sort_emails(self, emails, sort_by):
        if sort_by == 'date':
            emails.sort(key=lambda x: x.date)
        return emails
