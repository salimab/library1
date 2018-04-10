from django.shortcuts import render

def index(request):
    numbers = [1,2,3,4]
    name = "Salima"
    arg ={'myName' :name , 'numbers' :numbers}
    return render(request, 'personal/home.html',arg)
    #return render(request, 'home.html')

