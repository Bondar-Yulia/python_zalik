import unittest
from emailsys.EmailClient import EmailClient
from emailsys.Email import Email

class TestEmailClient(unittest.TestCase):

    def setUp(self):
        self.email_client = EmailClient()
        self.email_client.add_user('alice@example.com', 'password123')
        self.email_client.add_user('bob@example.com', 'password456')

    def test_send_email(self):
        self.email_client.send_email(
            sender_email='alice@example.com',
            recipient_email='bob@example.com',
            subject='Hello!',
            body='Hi Bob, just saying hello.',
            tags=['greeting']
        )
        bob = self.email_client.users['bob@example.com']
        self.assertEqual(len(bob.mailbox['default']['received']), 1)
        self.assertEqual(bob.mailbox['default']['received'][0].subject, 'Hello!')

    def test_create_folder(self):
        self.email_client.create_folder('bob@example.com', 'work')
        self.assertIn('work', self.email_client.users['bob@example.com'].mailbox['user_folders'])

    def test_clear_folder(self):
        self.email_client.create_folder('bob@example.com', 'work')
        email = Email('alice@example.com', 'bob@example.com', 'Project Update', 'The project is on track.', ['work'])
        self.email_client.add_email(email, 'bob@example.com', 'work')
        self.email_client.clear_folder('bob@example.com', 'work')
        self.assertEqual(len(self.email_client.users['bob@example.com'].mailbox['user_folders']['work']), 0)

    def test_delete_folder(self):
        self.email_client.create_folder('bob@example.com', 'work')
        self.email_client.delete_folder('bob@example.com', 'work')
        self.assertNotIn('work', self.email_client.users['bob@example.com'].mailbox['user_folders'])

    def test_block_sender(self):
        self.email_client.block_sender('bob@example.com', 'alice@example.com')
        bob = self.email_client.users['bob@example.com']
        self.assertIn('alice@example.com', bob.blocked_senders)

    def test_send_email_from_blocked_sender(self):
        self.email_client.block_sender('bob@example.com', 'alice@example.com')
        self.email_client.send_email(
            sender_email='alice@example.com',
            recipient_email='bob@example.com',
            subject='Another Hello!',
            body='Hi Bob, saying hello again.',
            tags=['greeting']
        )
        bob = self.email_client.users['bob@example.com']
        self.assertEqual(len(bob.mailbox['default']['received']), 0)

if __name__ == '__main__':
    unittest.main()
