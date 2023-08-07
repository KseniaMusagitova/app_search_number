from django.shortcuts import render, redirect
from .models import Dashboard
from .forms import DashboardForm


def dashboard(request):
    data = Dashboard.objects.order_by('-id')[:4]
    error = ''

    if request.method == "POST":
        form = DashboardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Invalid data entry form submission'
    else:
        form = DashboardForm()

    context = {
        'data': data,
        'form': form,
        'error': error
    }
    return render(request, 'testApp/index.html', context)
