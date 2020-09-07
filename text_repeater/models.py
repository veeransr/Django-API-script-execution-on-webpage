from django.db import models

# Create your models here.

class entervaluesTR(models.Model):
    category = 'Text_repeater'
    text = models.TextField()
    number = models.FloatField()


    def __float__(self):
        return self.category,self.text, self.number






class Snippet(models.Model):
    text = models.TextField()
    number = models.FloatField()


    def __float__(self):
        return self.text, self.number