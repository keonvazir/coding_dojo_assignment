from __future__ import unicode_literals
from django.db import models
import re


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 3 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 3 characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern           
            errors['email'] = ("Invalid email address!")
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 3 characters"
        if postData["password"] != postData["confirm_password"]:
            errors["confirm_pw"]= "Password does not match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    # email = models.EmailField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __repr__(self):
        return f"<User object: {self.first_name} {self.last_name} {self.email}>"



