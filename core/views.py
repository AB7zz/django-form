from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Database
# Create your views here.



def index(request):
    return render(request, 'index.html')

def registration(request):
    return render(request, 'registrationform.html')

def insert(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        schcol = request.POST['schcol']
        uni = request.POST['uni']
        seds = request.POST['seds']
        dob = request.POST['dob']
        proof = request.FILES.get('proof')
        # input8 = request.POST['input8']
        # input9 = request.POST['input9']

        db = Database.objects.create(
            name = name,
            email = email,
            phone = phone,
            schcol = schcol,
            uni = uni,
            seds = seds,
            dob = dob,
            proof = proof
            # input8 = input8,
            # input9 = input9
        )
        db.save()

        return redirect('/')
    return HttpResponse('<h1>Some error occurred...</h1>')



def display(request):
    all_inputs = []

    get_all_inputs = Database.objects.all()

    for data in get_all_inputs:
        print(data.name)
    return render(request, 'display.html', {'inputs' : get_all_inputs})