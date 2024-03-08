from django.shortcuts import render, redirect
from Interns.models import Workers
from Interns.forms import WorkersForm
# Create your views here.
def application_list(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = WorkersForm()
        else:
            application = Workers.objects.get(pk=id)
            form = WorkersForm(instance=application)
        return render(request, 'application_list.html', {'form': form})
    else:
        if id == 0:
            form = WorkersForm(request.POST)
        else:
            application = Workers.objects.get(pk=id)
            form = WorkersForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
        return redirect('/Interns/show')


def show(request):
    context = {'show': Workers.objects.all()}
    return render(request, 'show.html', context)