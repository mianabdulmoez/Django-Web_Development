from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Abdul Moeez'})
    # return render(request, 'home.html', {'name',input("Enter your name")})
    
# Fetching Data
# def add(request):
#     val1 = int(request.GET['num1'])
#     val2 = int(request.GET['num2'])
#     res = int(val1) + int(val2)
#     return render(request, 'result.html', {'result': res})

# Submitting Data
def add(request, methods=['POST']):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = int(val1) + int(val2)
    return render(request, 'result.html', {'result': res})
    # return render(request, 'result.html', {'result': res})