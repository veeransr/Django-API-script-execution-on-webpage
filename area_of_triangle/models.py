from django.db import models
from django.core import serializers
import json

# Create your models here.



class entervaluesAOFT1(models.Model):
    number1 = models.FloatField()
    number2 = models.FloatField()
    number3 = models.FloatField()

    def __float__(self):
        return self.number1, self.number2, self.number3


class Snippet(models.Model):
    number1 = models.FloatField()
    number2 = models.FloatField()
    number3 = models.FloatField()

    def __float__(self):
        return self.number1, self.number2, self.number3


# class data_process(models.Model):
#     s=  entervaluesAOFT.objects.all()
#     data = serializers.serialize("json",s)
#     p_data = json.loads(data)
#     a,b,c = list(p_data[-1]['fields'].values())
#     print(a,b,c)
#     s = (a + b + c) / 2
#     area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#     html = "<html><body>The area of triangle for the sides: %d, %d, %d is: %s "  % (a, b, c, int(area))
#     # return HttpResponseRedirect('/thanks/')
#     # return HttpResponse(html)
#     def __float__(self):
#         return self.html