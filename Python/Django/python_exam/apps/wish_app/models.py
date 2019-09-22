from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        for existing_user in User.objects.all():
            if existing_user.email == postData['email']:
                errors["email_exists"] = "We already have a user with this email"
        if len(postData['first_name']) < 2:
            errors["first_name"] = "first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "last name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern          
            errors['email'] = ("Invalid email address!")
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 3 characters"
        if postData["password"] != postData["confirm_password"]:
            errors["confirm_password"]= "Password does not match"
        return errors

class WishManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['new_item']) < 3:
            errors["item"] = "item should have at least 3 characters"
        if len(postData['new_description']) < 3:
            errors["description"] = "description should be at least 3 characters"
        return errors

class User(models.Model):
    objects = UserManager()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __repr__(self):
        return f"<User Object: {self.first_name} {self.last_name}, email: {self.email} password: {self.password}>"

class Wish(models.Model):
    objects = WishManager()
    user = models.ManyToManyField(User, related_name="wishes")
    item = models.CharField(max_length=255)
    granted = models.BooleanField(default=False)
    wished_for_by = models.ForeignKey(User, related_name="liked_wishes")
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __repr__(self):
        return f"<Wish object: {self.item}, description: {self.description}>"
