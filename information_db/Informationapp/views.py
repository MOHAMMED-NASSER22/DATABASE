from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Informationapp/base.html')


def other(request):
    return render(request, 'Informationapp/other.html')

def relative(request):
    return render(request, 'Informationapp/relative_url_templates.html')


def doctor(request):
    return render(request, 'Informationapp/doctor.html')


def patient(request):
    return render(request, 'Informationapp/patient.html')
