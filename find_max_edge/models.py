from django.db import models

# Create your models here.
class entervaluesFME(models.Model):
    number1 = models.FloatField()
    number2 = models.FloatField()


    def __float__(self):
        return self.number1, self.number2


class Snippet(models.Model):
    number1 = models.FloatField()
    number2 = models.FloatField()


    def __float__(self):
        return self.number1, self.number2