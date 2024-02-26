from django.shortcuts import render

def power_homepage(request):
    return render(request, 'Power_Tool_Pages/power_homepage.html')