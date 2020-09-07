#from /Users/veeranki/PycharmProjects/Django_projects/github/mysite/myapp/models import entervaluesAOFT1
from django.core import serializers
import json
import sys
import datetime

# def triangle_area_result (request):
# all_data = entervaluesAOFT1.objects.all()
#
# data = serializers.serialize("json", all_data)
# p_data = json.loads(data)
# first_side, second_side, third_side = list(p_data[-1]['fields'].values())
# a, b, c = first_side, second_side, third_side
# s = (a + b + c) / 2
# result = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# output = "The area of triangle for the sides: %d, %d, %d is: %s " % (first_side, second_side, third_side, int(result))
# print (output)
# if data coming from direct input

time = datetime.datetime.now()
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
s = (a + b + c) / 2

if s <= a or s <= b or s <= c:
    output = "The area of triangle for the sides: %d, %d, %d is: impossible triangle produced at time: %s" % (a, b, c,  time)
else:
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    output = "The area of triangle for the sides: %d, %d, %d is: %s produced at time: %s" % (a, b, c, area, time)


#output = 'hi %s %s %s current time is %s' %(sys.argv[1], sys.argv[2], sys.argv[3],time)
#output = 'hi %s %s %s %s current time is %s' %(a, b, c,s,time)
print(output)