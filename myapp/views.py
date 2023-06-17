from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def counter(request): 
    words = request.POST['words']
    word_count = len(words.split())
    return render(request, 'counter.html', {'amount': word_count})
 