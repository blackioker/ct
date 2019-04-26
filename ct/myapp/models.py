from django.db import models

# Create your models here.
class movie(models.Model):
    mname=models.CharField(max_length=20)
    actor=models.CharField(max_length=20)


    def __str__(self):
        return self.mname

    def short_actor(self):
        return self.actor[:50]+'....'

