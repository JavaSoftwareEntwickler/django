from django.shortcuts import render

# Create your views here.
def libri(request):
    return render(request, 'libri/tutorial_bootstrap.html')
