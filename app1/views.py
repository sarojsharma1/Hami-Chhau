from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def Home(request):
    return render(request, 'app1/home.html')

def Blog(request):
    return render(request, 'app1/blog.html')

def Yog_Guru(request):
    return render(request, 'app1/yog-guru.html')

def Psychologist(request):
    return render(request, 'app1/psychologist.html')

def Psychiatrist(request):
    return render(request, 'app1/psychiatrist.html')




def Profile(request):
    return render(request, 'app1/profile.html')

def SignUp(request):
    return render(request, 'app1/signup.html')
    
def Login(request):
    return render(request, 'app1/login.html')


