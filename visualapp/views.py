from django.shortcuts import render

# Create your views here.
def mainview(request):
    return render(request, 'visualapp/main.html')