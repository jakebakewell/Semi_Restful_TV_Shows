from django.db import models
from datetime import date, datetime

class ShowManager(models.Manager):


    def basic_validator(self, postData):
        errors = {}
        def is_title_used(title):
            if len(Show.objects.filter(title=title)) == 0:
                return False
            else:
                return True
        if is_title_used(postData['title']):
            errors["title_used"] = "Title is being used"
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['release_date']) > 0 and datetime.strptime(postData['release_date'], '%Y-%m-%d') > datetime.today():
            errors["release_date"] = "Release date must be in the past and a valid date"
        if len(postData['description']) > 0:
            if len(postData['description']) < 10:
                errors["description"] = "Description must be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
