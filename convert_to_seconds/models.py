from django.db import models

# Create your models here.

class entervaluesCTS(models.Model):
    days = models.IntegerField()
    hours = models.IntegerField()
    minutes = models.IntegerField()
    seconds = models.IntegerField()

    def __float__(self):
        return self.days, self.hours, self.minutes, self.seconds





class Snippet(models.Model):
    days = models.IntegerField()
    hours = models.IntegerField()
    minutes = models.IntegerField()
    seconds = models.IntegerField()

    def __float__(self):
        return self.days, self.hours, self.minutes, self.seconds