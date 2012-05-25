from django.db import models
from django.forms import ModelForm

MINUTE_CHOICES = (
    (5, '5'),
    (15, '15'),
    (30, '30'),
    (45, '45'),
    (60, '60'),
)

class Giraffeword(models.Model):
    url = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=400, null=True)
    added_date = models.DateTimeField('date added')
    duration = models.IntegerField(choices=MINUTE_CHOICES)

    def __unicode__(self):
        return self.url

class IPLog(models.Model):
    giraffeword = models.ForeignKey(Giraffeword)

    ip = models.CharField(max_length=20)
    added_date = models.DateTimeField('date logged')


class GiraffewordForm(ModelForm):
    class Meta:
        model = Giraffeword
        exclude = ('url', 'added_date')

