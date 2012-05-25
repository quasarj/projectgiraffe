from django.db import models

# Create your models here.
class Giraffeword(models.Model):
    url = models.CharField(max_length=200)
    password = models.CharField(max_length=400)
    added_date = models.DateTimeField('date added')

    def __unicode__(self):
        return self.url

