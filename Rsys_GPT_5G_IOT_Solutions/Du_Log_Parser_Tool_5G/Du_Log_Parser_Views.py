from django.shortcuts import render ,redirect
import re
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages

from Frequency_Tool_5G.utils import get_plot, get_single_plot
import matplotlib.pyplot as plt
import matplotlib
from django_matplotlib.fields import MatplotlibFigureField

import plotly.express as px

def du_log_homepage(request):
    return render(request,"Du_Log_Parser_Pages/du_log_homepage.html")


def du_log_parsing(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('freq_homepage')
    elif request.FILES.get('du_log_file'):
        du_log_file= request.FILES['du_log_file']
        matplotlib.use('Agg')
        du_log_text = du_log_file.read().decode('utf-8')
        # FileImport=open(du_log_text, "rt")
        FileImport = re.split('\n', du_log_text)
        CQI=[]
        MCS=[]
        SINR=[]
        TPUT=[]
        BLER=[]
        global chart_1,chart_2,chart_3,chart_4
       
        for line in FileImport:
            if "BLER_BASED_DL_CW_INFO_UPDATE" in line:
                TPUT1=re.findall('DL_LA_WINDOW_TPUT:' '-?\d+', line)
                TPUT2=re.findall('-?\d+' , str(TPUT1))
                #print(TPUT2)
                BLER1=re.findall('DL_LA_WINDOW_BLER:' '-?\d+', line)
                BLER2=re.findall('-?\d+' , str(BLER1))
                #print(BLER2)
                BLER.append(int(BLER2[0]))
                TPUT.append(int(TPUT2[0]))

            if "PUSCH_SINR_REPT" in line:
                SINR1=re.findall('PUSCH_SINR_REPT_INST:' '-?\d+', line)
                SINR2=re.findall('-?\d+' , str(SINR1))
                #print(SINR2)
                SINR.append(int(SINR2[0]))

            if "DL_LA_CAL_MCS" in line:

                DLCQI1=re.findall('DL_CQI:' '-?\d+', line)
                DLCQI2=re.findall('-?\d+' , str(DLCQI1))
                #print(DLCQI2)

                DLMCS1=re.findall('DL_MCS:' '-?\d+', line)
                DLMCS2=re.findall('-?\d+' , str(DLMCS1))
                #print(DL_MCS2)

                CQI.append(int(DLCQI2[0]))
                MCS.append(int(DLMCS2[0]))
        fig, graph = plt.subplots(2,2)
        # chart_1 = graph[0,0].plt.offline.plot(fig, auto_open = False, output_type="div")
        chart_1 = get_single_plot(SINR,'PUSCH vs SINR','SINR')

        graph[0,0].set_title('PUSCH-SINR')
        graph[0,0].color = 'k'

        # chart_2 = graph[1,0].plt.offline.plot(fig, auto_open = False, output_type="div")
        chart_2 =get_plot(CQI,MCS,'CQI vs MCS','CQI', 'MCS')
        graph[0,1].set_title('CQI vs MCS')

        # chart_3= graph[0,1].plt.offline.plot(fig, auto_open = False, output_type="div")
        chart_3 =get_plot(BLER, TPUT,'BLER vs TPUT', 'BLER', 'TPUT')
        graph[1,0].set_title('BLER vs TPUT')

        # chart_4 = graph[1,1].plt.offline.plot(fig, auto_open = False, output_type="div")
        chart_4 =get_plot(CQI, TPUT, 'CQI vs TPUT', 'CQI', 'TPUT')
        graph[1,1].set_title('CQI vs TPUT')
        # plt.show()
        charts=[
            chart_1,
            chart_2,
            chart_3,
            chart_4,
        ]
    return render(request,'Du_Log_Parser_Pages/du_log_homepage.html', {'charts':charts})
            
                
