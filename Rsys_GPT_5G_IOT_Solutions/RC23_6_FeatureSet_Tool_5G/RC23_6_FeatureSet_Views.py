from django.shortcuts import render

# Create your views here.
def featureset_homepage(request):
    return render(request,"RC23_6_FeatureSet_Pages/featureset.html")