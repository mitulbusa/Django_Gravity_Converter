from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "index.html")

def apitosg(request):
    if request.method == 'POST':
        apivalue = request.POST['apivalue']
        try:
            triall = float(apivalue)
            sgvalue = (141.5 +131.5)/ float(apivalue)
            return render(request, 'apitosg.html', {'sgvalue' : str(sgvalue)})
        except :
            errormessage = 'Value must be Positive Integer or Float'
            return render(request, 'apitosg.html', {'errormessage' : str(errormessage)})
    else:
        return render(request, 'apitosg.html')

def sgtoapi(request):
    if request.method == 'POST':
        sgvalue = request.POST['sgvalue']
        try:
            trial = float(sgvalue)
            apivalue = (141.5 / float(sgvalue)) - 131.5
            return render(request, 'sgtoapi.html', {'apivalue' : str(apivalue)})
        except :
            errormessage = 'Value must be Positive Integer or Float'
            return render(request, 'sgtoapi.html', {'errormessage' : str(errormessage)})
    else:
        return render(request, 'sgtoapi.html')

def contact(request):
    if request.method == 'POST':
        data = Contact()
        data.name = request.POST['name']
        data.email = request.POST['email']
        data.desc = request.POST['desc']
        data.save()
        message = "Submitted"
        return render(request, 'contact.html', {'message':message})
    else:
        return render(request, 'contact.html')
