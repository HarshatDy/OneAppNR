from django.shortcuts import render

# Create your views here.
def sunwave_homepage(request):
    return render(request,"Sunwave_IOT_Paramter_Pages/sunwave.html")