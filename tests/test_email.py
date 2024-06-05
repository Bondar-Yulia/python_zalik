import unittest
from datetime import datetime
from emailsys.Email import Email

class TestEmail(unittest.TestCase):

    def test_email_creation(self):
        email = Email('alice@example.com', 'bob@example.com', 'Hello', 'Hi Bob', ['greeting'])
        self.assertEqual(email.sender, 'alice@example.com')
        self.assertEqual(email.recipient, 'bob@example.com')
        self.assertEqual(email.subject, 'Hello')
        self.assertEqual(email.body, 'Hi Bob')
        self.assertIn('greeting', email.tags)
        self.assertIsInstance(email.date, datetime)

if __name__ == '__main__':
    unittest.main()
