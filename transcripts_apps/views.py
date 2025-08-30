from django.shortcuts import render


# Create your views here.

#H This view connects to the Home Page
def home(request):
    return render(request, 'index.html')