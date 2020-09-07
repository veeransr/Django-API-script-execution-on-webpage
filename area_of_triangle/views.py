from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import entervaluesAOFT, sippetform
from .models import entervaluesAOFT1
from django.core import serializers
from .serializers import resultSerializer
from django.views.generic import View
# from . script import triangle_area_result
from django.views.decorators.csrf import csrf_exempt
import json,requests
from subprocess import Popen, PIPE, STDOUT, call, run
import sys
import requests
# from . utils import *

#https://html.developreference.com/article/18101258/Button+acts+as+both+%e2%80%9csubmit%e2%80%9d+and+%e2%80%9chref%e2%80%9d
#https://www.youtube.com/watch?v=ejJ-2oz4AgI
#https://anvil.works/blog/python-in-the-browser-talk


def area_of_triangle(request):

    if request.method == 'POST':
        form = entervaluesAOFT(request.POST)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # number1 = form.cleaned_data ['number1']
            # number2 = form.cleaned_data ['number2']
            # number3 = form.cleaned_data['number3']
            # print( number1, number2, number3 )

    form = entervaluesAOFT()
    return render(request, 'myapp/form.html', {'form':form})
    # return number1,number2,number3

def snippet_details(request):

    if request.method == 'POST':
        form = sippetform(request.POST)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # number1 = form.cleaned_data['number1']
            # number2 = form.cleaned_data['number2']
            # number3 = form.cleaned_data['number3']
            # print(number1, number2, number3)

    form = sippetform()
    return render(request, 'myapp/form.html', {'form': form})
    # return number1,number2,number3



def button(request):
    return render(request, 'home.html')



# def output(request):
#     data = requests.get('')
#     print(data.text)
#     data = data.text
#     return render(request, 'home.html', {'data': data})


# def external(request):
#     # input = request.POST.get('param')
#     out = run(sys.executable, ['script.py', input], shell = False, stdout = PIPE )
#     print(out)
#
#     return render(request,'/myapp/form.html', {'data': out.stdout} )

def external(request):
    inp1 = request.POST.get('param1')
    inp2 = request.POST.get('param2')
    inp3 = request.POST.get('param3')
    out = run(['python', "//Users//veeranki//PycharmProjects//Django_projects//myforms//myapp//utils.py", inp1, inp2, inp3],  capture_output=True, shell = False)
    print(out)
    return render(request,'myapp/form.html', {'data1': out.stdout.decode("utf-8")} )

# def external(request):
#     # inp = request.POST.get('param')
#     out = triangle_area_result()
#     print(out)
#
#     return render(request,'/myapp/form.html', {'data1': out} )








# all_data = entervaluesAOFT1.objects.all()
# data = serializers.serialize("json", all_data)
# p_data = json.loads(data)
# first_side,second_side, third_side = list(p_data[-1]['fields'].values())
# a,b,c = first_side,second_side, third_side
# s = (a + b + c) / 2
# triangle_area_result = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# print(triangle_area_result)



class result_for_Triangle_area (APIView):

    def get(self, request):
        all_data = entervaluesAOFT1.objects.all()



        data = [subprocess.call (['python', 'script.py'])]
         # dict = {'name': 'Monty', 'age': 42, 'food': 'spam'}
         # # x = {
         # #     "name": "John",
         # #     "age": 30,
         # #     "city": "New York"
         # # }

        # r1 = json.dumps(x)

        r2 = json.dumps(data)

         # serializer = resultSerializer(x, many=True)
        return Response(r2)


    def post(self):
        pass

def output(request):
    data = requests.get(entervaluesAOFT1.objects.all())

    return render(request, 'myapp/form.html', {'data':data} )
# def result_view(request):
#
#     if request.method == 'POST':
#         form = data_process(request.POST)
#         if form.is_valid():
#             form.save()
#
#
#     form = data_process()
#     return render(request, 'form.html', {'form': form})













# def getvaluesAOFT(request):
#     if request.method == 'POST':
#         data = request.POST.list()
#         a = data[0]
#         b= data[1]
#         c= data[2]
#         # if form.is_valid():
#             # a = request.POST.get('number1', '')
#             # b = request.POST.get('number2', '')
#             # c = request.POST.get('number3', '')
#             # print(a,b,c)
#             # return a,b,c
#             # print(form.cleaned_data[number1, ])
#             return HttpResponseRedirect('/thanks/')  # Redirect after POST

# a,b,c = getvaluesAOFT()
# s = (a + b + c) / 2
# area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# html = "<html><body>The area of triangle for the sides: %d, %d, %d is: %s " % (a, b, c, int(area))
# # return HttpResponse(html)

# def data_process(request):
#     s=  entervaluesAOFT.objects.all()
#     data = serializers.serialize("json",s)
#     p_data = json.loads(data)
#     a,b,c = list(p_data[-1]['fields'].values())
#     print(a,b,c)
#     s = (a + b + c) / 2
#     area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#     html = "<html><body>The area of triangle for the sides: %d, %d, %d is: %s "  % (a, b, c, int(area))
    # return HttpResponseRedirect('/thanks/')
    # return HttpResponse(html)






    # while True:
    #     x = input('enter the length of the three sides of a triangle seperated by space').split()
    #     if len(x) < 3 or len(x) > 3:
    #         print('You gave less than or more three values, please try again')
    #         continue
    #     else:
    #         # a = float(x[0])
    #         # b = float(x[1])
    #         # c = float(x[2])
# a,b,c = area_of_triangle(request)
# if 0 in [a, b, c]:
#     print(
#         'you entered  one or more zero values, should have a valid length on each sides, please try again')
#     # continue
# else:
#     a = 12
#     b = 13
#     c = 14
#     s = (a + b + c) / 2
#     area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#     html = "<html><body>The area of triangle for the sides: %d, %d, %d is: %s "  % (a, b, c, int(area))
#     # return HttpResponse (html)

