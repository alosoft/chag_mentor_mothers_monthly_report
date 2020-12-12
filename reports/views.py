from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from reports import models, forms
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):

    if request.GET.get('logout') is not None:
        logout_user(request)

    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_user(request, user)
        else:
            messages.error(request, 'Invalid Credentials')
    if request.user.is_authenticated:
        return HttpResponseRedirect('dashboard')

    return render(request, 'login.html')

@login_required
def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html', {
        'user': user
    })

@login_required
def reports(request):
    return render(request, 'reports.html')

@login_required
def add_report(request):
    return render(request, 'add_report.html', {
        'user': request.user
    })

@login_required
def create(request):
    if request.method == 'GET':
        return redirect('add_report')
    else:
        new_data = forms.ClientsNewlyAndUniquelyEnrolledIntoMMSCareAndSupportForm(request.POST)
        print(new_data)
    return HttpResponse('success')


@login_required
def report(request):
    pk = request.GET.get('pk')
    single_report = None
    # try:
    #     single_report = models.MonthlyReport.objects.get(pk=pk, hospital=request.user)
    # except models.MonthlyReport.DoesNotExist:
    #     raise Http404
    
    return render(request, 'report.html', {
        'report': single_report
    })


def reset(request):
    return render(request, 'reset.html')