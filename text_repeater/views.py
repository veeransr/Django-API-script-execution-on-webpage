def snippet_details(request):

    if request.method == 'POST':
        form = snippetform(request.POST)
        if form.is_valid():
            form.save()


    form = snippetform()
    return render(request, 'form.html', {'form': form})


def external(request):
    inp1 = request.POST.get('param1')
    inp2 = request.POST.get('param2')


    out = run(['python', "//Users//veeranki//PycharmProjects//Django_projects//myforms//text_repeater//utils.py", inp1, inp2],  capture_output=True, shell = False)
    print(out)
    return render(request,'text_repeater/form.html', {'data1': out.stdout.decode("utf-8")} )
