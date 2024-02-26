from django.shortcuts import render

# Create your views here.
def nec_oran_homepage(request):
    return render(request,"NEC_ORAN_CUSPlane_SOC_8T8R_NEC_RU_Pages/nec_oran.html")