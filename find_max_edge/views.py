from django.shortcuts import render
from django.http import HttpResponse
from .forms import entervaluesFME, snippetform
from subprocess import run


def find_max_edge(request):

    if request.method == 'POST':
        form = entervaluesFME(request.POST)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # number1 = form.cleaned_data ['First Side of triangle']
            # number2 = form.cleaned_data ['Second Side of triangle']
            #
            # print( number1, number2 )

    form = entervaluesFME()
    return render(request, 'find_max_edge/form.html', {'form':form})
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

    out = run(['python', "//Users//veeranki//PycharmProjects//Django_projects//myforms//find_max_edge//utils.py", inp1, inp2],  capture_output=True, shell = False)
    print(out)
    return render(request,'find_max_edge/form.html', {'data1': out.stdout.decode("utf-8")} )