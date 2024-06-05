import unittest
from emailsys.EmailSystem import EmailSystem
from emailsys.EmailUser import User
from emailsys.Email import Email

class TestEmailSystem(unittest.TestCase):

    def setUp(self):
        self.email_system = EmailSystem()
        self.email_system.add_user('alice@example.com', 'password123')
        self.email_system.add_user('bob@example.com', 'password456')

    def test_add_user(self):
        self.email_system.add_user('charlie@example.com', 'password789')
        self.assertIn('charlie@example.com', self.email_system.users)

    def test_delete_user(self):
        self.email_system.delete_user('alice@example.com')
        self.assertNotIn('alice@example.com', self.email_system.users)

    def test_add_email(self):
        email = Email('alice@example.com', 'bob@example.com', 'Hello', 'Hi Bob', ['greeting'])
        self.email_system.add_email(email, 'bob@example.com', 'received')
        bob = self.email_system.users['bob@example.com']
        self.assertIn(email, bob.mailbox['default']['received'])

    def test_delete_email(self):
        email = Email('alice@example.com', 'bob@example.com', 'Hello', 'Hi Bob', ['greeting'])
        self.email_system.add_email(email, 'bob@example.com', 'received')
        self.email_system.delete_email('bob@example.com', email.id)
        bob = self.email_system.users['bob@example.com']
        self.assertNotIn(email, bob.mailbox['default']['received'])

    def test_search_emails(self):
        email = Email('alice@example.com', 'bob@example.com', 'Hello', 'Hi Bob', ['greeting'])
        self.email_system.add_email(email, 'bob@example.com', 'received')
        results = self.email_system.search_emails('bob@example.com', subject='Hello')
        self.assertIn(email, results)

    def test_sort_emails(self):
        email1 = Email('alice@example.com', 'bob@example.com', 'Hello', 'Hi Bob', ['greeting'])
        email2 = Email('charlie@example.com', 'bob@example.com', 'Meeting', 'Reminder', ['work'])
        self.email_system.add_email(email1, 'bob@example.com', 'received')
        self.email_system.add_email(email2, 'bob@example.com', 'received')
        results = self.email_system.search_emails('bob@example.com')
        sorted_emails = self.email_system.sort_emails(results, 'date')
        self.assertEqual(sorted_emails[0], email1)

if __name__ == '__main__':
    unittest.main()
