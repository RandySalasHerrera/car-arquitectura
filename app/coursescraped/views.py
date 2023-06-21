from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def scraper(request):
    return render(request, 'scraper.html')
