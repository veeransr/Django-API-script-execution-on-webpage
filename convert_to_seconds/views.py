from django.shortcuts import render
from django.http import HttpResponse
from .forms import entervaluesCTS, snippetform
from subprocess import run


def convert_to_seconds(request):

    if request.method == 'POST':
        form = entervaluesCTS(request.POST)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # days = form.cleaned_data ['day']
            # hours = form.cleaned_data ['hours']
            # minutes = form.cleaned_data['minutes']
            # seconds = form.cleaned_data['seconds']
            # print( days, hours, minutes, seconds )

    form = entervaluesCTS()
    return render(request, 'convert_to_seconds/form.html', {'form':form})
    # return number1,number2,number3

def snippet_details(request):

    if request.method == 'POST':
        form = snippetform(request.POST)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # number1 = form.cleaned_data['number1']
            # number2 = form.cleaned_data['number2']
            # number3 = form.cleaned_data['number3']
            # print(number1, number2, number3)

    form = snippetform()
    return render(request, 'form.html', {'form': form})
    # return number1,number2,number3


def external(request):
    inp1 = request.POST.get('param1')
    inp2 = request.POST.get('param2')
    inp3 = request.POST.get('param3')
    inp4 = request.POST.get('param4')

    out = run(['python', "//Users//veeranki//PycharmProjects//Django_projects//myforms//convert_to_seconds//utils.py", inp1, inp2, inp3, inp4],  capture_output=True, shell = False)
    print(out)
    return render(request,'convert_to_seconds/form.html', {'data1': out.stdout.decode("utf-8")} )