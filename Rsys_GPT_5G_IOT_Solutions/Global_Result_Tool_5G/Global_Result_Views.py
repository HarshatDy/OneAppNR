from django.shortcuts import render

# Create your views here.
def global_result_homepage(request):
    return render(request,"Global_Result_Pages/global_result_homepage.html")

def global_result(request):
    return render(request,"Global_Result_Pages/global_result_homepage.html")