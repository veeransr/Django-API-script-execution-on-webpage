from django.shortcuts import get_object_or_404, render
import requests


def button(request):
    return render(request, 'home.html')



def output(request):
    data = requests.get('https://html.developreference.com/article/18101258/Button+acts+as+both+%e2%80%9csubmit%e2%80%9d+and+%e2%80%9chref%e2%80%9d')
    print(data.text)
    data = data.text
    return render(request, 'home.html', {'data': data})