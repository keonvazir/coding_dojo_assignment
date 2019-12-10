from django.db import models

class Roster(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Roster object: {self.title} {self.description}>"


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    notes = models.TextField()
    rosters = models.ManyToManyField(Roster, related_name="users")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<User object: {self.first_name} {self.last_name} {self.notes}>"



