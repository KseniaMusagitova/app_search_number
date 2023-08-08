from django.shortcuts import render, redirect
from .models import Dashboard
from .forms import DashboardForm, SearchForm


def dashboard(request):
    data = Dashboard.objects.order_by('-id')[:4]
    error = ''

    if request.method == "POST":
        form = DashboardForm(request.POST)
        searchform = SearchForm(request.POST)
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
        'error': error,

    }
    return render(request, 'testApp/index.html', context)


def search_serial_number(request):
    error = ''
    search_result = None

    if request.method == "POST":
        searchform = SearchForm(request.POST)

        if searchform.is_valid():
            search_serial_number = searchform.cleaned_data['serial_number']
            search_result = Dashboard.objects.filter(serial_number=search_serial_number).first()

        else:
            error = 'Invalid search form submission'
    else:
        searchform = SearchForm()

    context = {
        'searchform': searchform,
        'error': error,
        'search_result': search_result,
    }
    return render(request, 'testApp/search_result.html', context)