from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'intro/introduction.html')


def alg(request):
    return render(request, 'intro/algorithm.html')
