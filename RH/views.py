from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Rproject/index.html')

def addemploye(request):
    return render(request,'Rproject/addemploye.html')