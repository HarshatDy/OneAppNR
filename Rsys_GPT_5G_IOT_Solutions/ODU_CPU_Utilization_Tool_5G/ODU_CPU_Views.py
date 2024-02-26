from django.shortcuts import render,redirect
import matplotlib.pyplot as plt
from Frequency_Tool_5G.utils import get_plot, get_single_plot, get_line, only_plot,get_graph

# Create your views here.
import re

import pandas as pd

def odu_cpu_homepage(request):
    return render(request,"ODU_CPU_Utilization_Pages/odu_cpu_homepage.html")

def odu_cpu_calculation(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('freq_homepage')
    elif request.FILES.get('odu_cpu_file'):
        odu_cpu_file= request.FILES['odu_cpu_file']
        
        # Set the figure size
        plt.rcParams["figure.figsize"] = [7.00, 3.50]
        plt.rcParams["figure.autolayout"] = True
        # Make a list of columns
        columns = ['%CPU','P','TIME+','COMMAND']
        # Read a CSV file
        df = pd.read_csv(odu_cpu_file, usecols=columns)
        # Plot the lines
        chart_ply = only_plot(df)
        # chart = get_line(df,"title","namex","namey")
        # chart = get_single_plot(df,"title","x")
        # df.plot()
        # chart = 
        chart = chart_ply.to_html(full_html=False, default_height='100%', default_width='100%')


        # plt.show()
        return render(request, "ODU_CPU_Utilization_Pages/odu_cpu_homepage.html",{"charts":chart})
