from django.db import models

# Create your models here.
import hashlib

class UserForm:
    def __init__(self, username, email, password, password_repeat):
        self.username = username
        self.email = email
        self.__password = password
        self.__password_repeat = password_repeat

    @property
    def password(self):
        return self.__password

    @property
    def password_repeat(self):
        return self.__password_repeat

    def is_valid(self):
        errors = []
        if not self.username or not self.email or not self.__password or not self.__password_repeat:
            errors.append('Todos os campos devem ser preenchidos.')
        if len(self.__password) < 6:
            errors.append('Senha deve conter ao menos 6 caractéres.')
        if self.__password != self.__password_repeat:
            errors.append('Senhas não coincidem.')
            
        return errors if errors else True
        
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__hashed_password = self.__hash_password(password)

    @staticmethod
    def __hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_hash_password(self, password):
        return self.__hash_password(password) == self.__hashed_password

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'hashed_password': self.__hashed_password
        }
