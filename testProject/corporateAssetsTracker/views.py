from django.shortcuts import render

# Create your views here.
def index(request):
    # return a http response
    return render(request, 'index.html')
