from django.shortcuts import render

def subjectProfile(request):
    return render(request, 'subjectProfile.html')

def history(request):
    return  render(request, 'history.html')

def study(request):
    return render(request,'study.html')


def interests(request):
    return  render(request, 'interests.html')

def career(request):
    return  render(request, 'career.html')

def rolemodel(request):
    return  render(request, 'rolemodel.html')


