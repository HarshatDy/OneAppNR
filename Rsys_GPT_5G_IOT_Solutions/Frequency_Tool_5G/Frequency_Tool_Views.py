from django.shortcuts import render ,redirect
import re
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages

from .utils import get_plot, get_single_plot
import matplotlib.pyplot as plt
import matplotlib
from django_matplotlib.fields import MatplotlibFigureField

import pandas as pd  
from tabulate import tabulate
import plotly.express as px

def freq_homepage(request):
    return render(request,"Frequency_Tool_Pages/freq_page.html")


def freq_calculation(request):
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
    return render(request,'Frequency_Tool_Pages/freq_page.html', {'charts':charts})
            

def freq_table(request):

    freq_table_file = request.FILES.get('freq_table_file')
    def freqToArfcn(freq):
        arfcn_ = 0
        if freq < 3000000:
            arfcn_ = (freq - 0)/5 + 0                                                                                            
                                                                                                                                
        elif(freq <= 24250000):                                                                                              
            arfcn_ = (freq - 3000000)/15 + 600000                                                                              

        elif (freq <= 100000000):                                                                                             
            arfcn_ = (freq - 24250080)/60 + 2016667
        return arfcn_

    def arfcnToFreq(arfcn):
        freq_ = 0;                                                                                                                                                                                                                                

        if (arfcn <= 599999):                                                                                                            
            freq_ = 0 + 5 * (arfcn - 0)

        elif(arfcn <= 2016666):                                                                                                                                                                                                                    
            freq_ = 3000000 + 15 * (arfcn - 600000)

        elif (arfcn <= 3279165):                                                                                                                                                                                                                    
            freq_ = 24250080 + 60 * (arfcn - 2016667) 
        return freq_

    # freq_table_file = request.POST.get('freq_table_file')
    print(freq_table_file)
    df = pd.read_excel(freq_table_file) 

    #GSCN to FREQ convertor
    GSCN = request.POST.get('gscn_value')
    table1 = []
    found = False
    table1.append(['BAND', 'SCS', 'GSCN', 'N', 'SS_FREQ', 'ARFCN'])
    for _, row in df.iterrows():
        if((int(GSCN) >= row.GSCN_MIN) and (int(GSCN) <= row.GSCN_MAX)):
            found = True
            M = 3
            if((row.SS_FRQ_MIN >=0) and (row.SS_FRQ_MAX < 3000)):
                N = int(int(GSCN)/3)
                SSFREQ_ = (N * 1200 + M * 50)

            elif((row.SS_FRQ_MIN >=3000) and (row.SS_FRQ_MAX < 24250)):
                N = int(int(GSCN) - 7499)
                SSFREQ_ = (3000000 + N * 1440)

            elif((row.SS_FRQ_MIN >=24250) and (row.SS_FRQ_MAX < 100000)):
                N = int(int(GSCN) - 22256)
                SSFREQ_ = (24250080 + N * 17280)

            M = 3
            #SSFREQ_ = (N * 1200 + M *50 )
            #print("ssfrq", SSFREQ_)
            if(((SSFREQ_/1000 >= row.SS_FRQ_MIN) and (SSFREQ_/1000 <= row.SS_FRQ_MAX)) == False):
                found =False
                #print("hitting false")
                continue
            ARFCN_ = freqToArfcn(SSFREQ_)
            table1.append([row.BAND, row.SCS, int(GSCN), N, SSFREQ_ /1000, ARFCN_])
    if(found):
        print("GSCN to Frequency / ARFCN conversion")
        charts= table1
        # charts = tabulate(table1, tablefmt='grid')
        print("=========================")
        print(charts)
        print(tabulate(table1, tablefmt='grid'))
        return render(request,'Frequency_Tool_Pages/freq_page.html', {'charts':charts})
        
    else:
        print("invalid GSCN ")
        return render(request,'Frequency_Tool_Pages/freq_page.html')

def freq_value(request):
        freq_table_file = request.FILES.get('freq_table_file')
        df = pd.read_excel(freq_table_file)
        def freqToArfcn(freq):
            arfcn_ = 0
            if freq < 3000000:
                arfcn_ = (freq - 0)/5 + 0                                                                                            
                                                                                                                                    
            elif(freq <= 24250000):                                                                                              
                arfcn_ = (freq - 3000000)/15 + 600000                                                                              

            elif (freq <= 100000000):                                                                                             
                arfcn_ = (freq - 24250080)/60 + 2016667
            return arfcn_ 
        FREQ = input("enter FREQ value : ")
        table2 = []
        found = 0
        table2.append(['BAND', 'SCS', 'GSCN', 'N', 'SS_FREQ', 'ARFCN'])
        for _, row in df.iterrows():  
            if((float(FREQ) >= row.SS_FRQ_MIN) and (float(FREQ) <= row.SS_FRQ_MAX)):
                found = True 
                M = 3
                if((row.SS_FRQ_MIN >= 0) and (row.SS_FRQ_MAX < 3000)):
                    N = int(((float(FREQ)*1000) - (M * 50))/1200)
                    GSCN_ = N * 3
                elif((row.SS_FRQ_MIN >= 3000) and (row.SS_FRQ_MAX < 24250)):
                    N = int(((float(FREQ)*1000) - 3000000)/(1440))
                    GSCN_ = N + 7499
                elif((row.SS_FRQ_MIN >= 24250) and (row.SS_FRQ_MAX < 100000)):
                    N = int(((float(FREQ)*1000) - 24250080)/(17280))
                    GSCN_ = N + 22256
                
                if(((GSCN_ >= row.GSCN_MIN) and (GSCN_ <= row.GSCN_MAX)) == False):
                    found =False
                    print("GSCN_ = ",GSCN_)
                    continue

                
                ARFCN_ = freqToArfcn(float(FREQ)*1000)
                #print("appending band ",row.BAND)
                table2.append([row.BAND, row.SCS, GSCN_, N, float(FREQ), ARFCN_])
            
        if(found):
            print("Frequency to GSCN / ARFCN conversion")
            print(tabulate(table2, tablefmt='grid'))
            charts = tabulate(table2, tablefmt='grid')
            return render(request,'Frequency_Tool_Pages/freq_page.html', {'charts':charts})
        else:
            print("invalid FREQ or Requested GSCN not valid")   
            return render(request,'Frequency_Tool_Pages/freq_page.html')

                
def freq_value_homepage(request):
    return render(request,'Frequency_Tool_Pages/freq_value.html')
