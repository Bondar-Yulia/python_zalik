from abc import ABC, abstractmethod

class EmailSystemBase(ABC):
    @abstractmethod
    def add_user(self, email, password):
        pass

    @abstractmethod
    def delete_user(self, email):
        pass

    @abstractmethod
    def add_email(self, email, user_email, folder_name='received'):
        pass

    @abstractmethod
    def delete_email(self, user_email, email_id):
        pass

    @abstractmethod
    def search_emails(self, user_email, **kwargs):
        pass

    @abstractmethod
    def sort_emails(self, emails, sort_by):
        pass
