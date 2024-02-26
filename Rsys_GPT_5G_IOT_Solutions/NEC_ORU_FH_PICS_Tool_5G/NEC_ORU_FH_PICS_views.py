from django.shortcuts import render

# Create your views here.
def nec_oru_homepage(request):
    return render(request,"NEC_ORU_FH_PICS_Pages/nec_fh.html")