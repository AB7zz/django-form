from django.shortcuts import render
from django.http import HttpResponse
from .models import Database
# Create your views here.



def index(request):
    return render(request, 'index.html')

def insert(request):
    if request.method == "POST":
        input1 = request.POST['input1']
        input2 = request.POST['input2']
        input3 = request.POST['input3']
        input4 = request.POST['input4']
        input5 = request.POST['input5']
        input6 = request.POST['input6']
        input7 = request.POST['input7']
        # input8 = request.POST['input8']
        # input9 = request.POST['input9']

        db = Database.objects.create(
            input1 = input1,
            input2 = input2,
            input3 = input3,
            input4 = input4,
            input5 = input5,
            input6 = input6,
            input7 = input7,
            # input8 = input8,
            # input9 = input9
        )
        db.save()

        return redirect('/')
    return HttpResponse('<h1>Some error occurred...</h1>')
