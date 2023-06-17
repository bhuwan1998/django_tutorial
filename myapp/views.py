from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # dynamic data - for each user they have their own data 
    # make classes 
    context = {
        # dictionary 
        'name' : 'Patrick', 
        'age': '23', 
        'nationality': 'British'
    }
    name = 'Patrick'
    return render(request, 'index.html', context)
 