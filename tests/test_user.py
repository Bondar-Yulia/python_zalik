import unittest
from emailsys.EmailUser import User

class TestUser(unittest.TestCase):

    def test_user_creation(self):
        user = User('alice@example.com', 'password123')
        self.assertEqual(user.email, 'alice@example.com')
        self.assertEqual(user.password, 'password123')
        self.assertIn('sent', user.mailbox['default'])
        self.assertIn('received', user.mailbox['default'])
        self.assertIn('spam', user.mailbox['default'])
        self.assertEqual(len(user.blocked_senders), 0)

if __name__ == '__main__':
    unittest.main()
