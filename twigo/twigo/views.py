from django.shortcuts import render

# Create your views here.
def layout_home(request):
    return render(request, 'twigo/layout.html')
