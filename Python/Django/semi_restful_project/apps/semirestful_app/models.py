from __future__ import unicode_literals
from django.db import models

class RestfulManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['new_title']) < 5:
            errors["new_title"] = "Show name should be at least 5 characters"
        if len(postData['new_network']) < 2:
            errors["new_network"] = "Show network should be at least 1 character"
        return errors

class Restful(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RestfulManager()
    def __repr__(self):
        return f"<Restful object: {self.id} {self.title} {self.network} {self.release_date}>"

