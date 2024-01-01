from django.db import models

# Create your models here.
class Filmapp(models.Model):
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    year = models.IntegerField()
    cover=models.FileField(upload_to='fimapp/cover',null=True,blank=True)
