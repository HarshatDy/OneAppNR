from django.shortcuts import render ,redirect
import re
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
import matplotlib.pyplot as plt
from datetime import datetime
import sys
import numpy as np

from Frequency_Tool_5G.utils import get_plot, get_single_plot
import matplotlib.pyplot as plt
import matplotlib
from django_matplotlib.fields import MatplotlibFigureField

import plotly.express as px

def ota_algo_homepage(request):
    return render(request,"OTA_Algo_Pages/ota_algo_homepage.html")


def ota_algo_calculation(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('freq_homepage')
    elif request.FILES.get('du_log_file'):
        log_file= request.FILES['du_log_file']
        # print(log_file)
        matplotlib.use('Agg')
        plot_type_1= 1
        is_Templated_1 =1
        #!/usr/bin/python
        global chart_1, chart_2, chart_3, chart
        def conv_sfn(timeinfo):
            dummyslot = {0:0,1:0,2:0,3:0,4:0,5:5,6:5,7:5,8:5,9:5}
            #return int(timeinfo.microsecond/1000)*10 + dummyslot[int(timeinfo.microsecond/100)%10] + timeinfo.second*10000 + timeinfo.minute*60*10000 + timeinfo.hour*60*60*10000
            return int(timeinfo.microsecond/1000)*1000 + int(timeinfo.microsecond%1000) + timeinfo.second*1000000 + timeinfo.minute*60*1000000 + timeinfo.hour*60*60*1000000

        #ADD more templates which could be helpful for log analysis
        #1:("ULLA","UL_LA_CAL_MCS-DELTA_AGE_100,OLLA_OFFSET_100,DELTA_TPC_100,ALGO_SINR_SRS_REP_NOISE_PDO,EFF_SINR_ALGO_SINR_OLLA_AGING_DELTA_TPC,MCS:PUSCH_SINR_REPT-PUSCH_SINR_REPT_INST"),
        #1:("ULLA","UL_LA_CAL_MCS-DELTA_AGE_100,OLLA_OFFSET_100,SEED_OLLA_100,ALGO_SINR_SRS_REP_NOISE_PDO,MCS:PUSCH_SINR_REPT-PUSCH_SINR_REPT_INST"),
        #1:("ULLA","UL_LA_CAL_MCS-DELTA_AGE_100,OLLA_OFFSET_100,SEED_OLLA_100,ALGO_SINR_SRS_REP_NOISE_PDO,MCS"),
        #1:("ULLA","ESTIMITED_ALOG_OUTPUT-RI,PMI:BLER_BASED_CW_INFO_UPDATE-WINDOW_BLER:UL_LA_CAL_MCS-SEED_OLLA_100,ALGO_SINR_SRS_REP_NOISE_PDO,MCS"),
        #4:("DLLA","DL_LA_CAL_MCS-DL_DELTA_AGE_100,DL_OLLA_OFFSET_100,DL_CQI,DL_MCS:BLER_BASED_DL_CW_INFO_UPDATE-DL_LA_COMPARE_SEED_OLLA_100"),
        #4:("DLLA","DL_LA_CAL_MCS-DL_DELTA_AGE_100,DL_OLLA_OFFSET_100,DL_CQI,DL_MCS:BLER_BASED_DL_CW_INFO_UPDATE-DL_LA_WINDOW_BLER"),
        #4:("DLLA","DL_LA_CAL_MCS-DL_OLLA_OFFSET_100,DL_CQI,DL_MCS:BLER_BASED_DL_CW_INFO_UPDATE-DL_LA_COMPARE_SEED_OLLA_100,DL_LA_WINDOW_BLER:LA_HARQ_FEEDBACK-DL_LA_MCS_STATE,DL_LA_FEEDBACK:UL_LA_CAL_MCS-DELTA_AGE_100"),
        #1:("ULLA","UL_LA_CAL_MCS-DELTA_AGE_100,OLLA_OFFSET_100,SEED_OLLA_100,ALGO_SINR_SRS_REP_NOISE_PDO:UL_LA_CRC_PASS_INFO-UL_NUM_PRB_REQ,UL_IMCS,UL_LA_MCS_STATE:BLER_BASED_CW_INFO_UPDATE-ACK_CNT,NACK_CNT,WINDOW_BLER"),
        #1:("ULLA","UL_LA_CAL_MCS-DELTA_AGE_100,ALGO_SINR_SRS_REP_NOISE_PDO:BLER_BASED_CW_INFO_UPDATE-ACK_CNT,NACK_CNT,WINDOW_BLER:UL_LA_COMPARE_SINR-MCS,BASE_MCS:UL_LA_CRC_PASS_INFO-UL_NUM_PRB_REQ"),
        #1:("ULLA","UL_LA_CAL_MCS-DELTA_AGE_100,OLLA_OFFSET_100,SEED_OLLA_100,ALGO_SINR_SRS_REP_NOISE_PDO:UL_LA_CRC_PASS_INFO-UL_NUM_PRB_REQ,UL_IMCS,UL_LA_MCS_STATE"),
        #UL_LA_COMPARE_SINR:UE_ID:94500160010017017:MCS:12:BASE_MCS:12:UL_LA_COMPARE_PUSCH_SINR_100:550:UL_LA_COMPARE_SRS_SINR_100
        plot_template = {
        1:("ULLA","UL_LA_CAL_MCS-OLLA_OFFSET_100,DELTA_AGE_100,SEED_OLLA_100,ULLA_ALGO_SINR,MCS:BLER_BASED_CW_INFO_UPDATE-WINDOW_BLER"),
        2:("CLPC","RG_SCH_PWR_GET_PUSCH_TPC-TPC,TARGET_SINR,WIDEBAND_SINR,PATHLOSS,PHR,ACCUMULATED_TPC"),
        3:("DLLA","DL_LA_CAL_MCS-DL_CQI,DL_MCS,DL_DELTA_AGE_100,DL_OLLA_OFFSET_100,DL_LA_COMPARE_SEED_OLLA_100:BLER_BASED_DL_CW_INFO_UPDATE-DL_LA_WINDOW_BLER"),
        }

        def get_start_time(filename):
            # print(filename)        
            with open(filename.read()) as src_file:
                line = src_file.readline()
                line = [x.strip(' ').strip('[') for x in line.split(']')]
                return (conv_sfn(datetime.strptime(line[0],'%d/%m/%Y %H:%M:%S.%f')))

        def disp_help():
            print("L2Analyser.py <filename> <Plot-type(1->TimeSeries Plot : 2->X-Y Plot)>  <Input(1=> isTemplated : 2=>Custom Plot)> ")

        def validate_input_args():
            isTemplated = 0
            filename = log_file
            plot_type = plot_type_1
            if plot_type == 1:
                isTemplated = is_Templated_1
            return [filename,plot_type,isTemplated]

        class PlotConfig:
            filename = None
            plot_type = None
            isTemplated = None
            plot_config = None

            def __init__(self):
                self.get_input()

            def disp_help_template(self):
                if self.isTemplated == 1:
                    for index,data in plot_template.items():
                        print(str(index) + " => " + data[0])

            def get_templated_config(self):
                self.disp_help_template()
                ip = int(input(">>Please input the plot choice\n>>"))
                while ip not in plot_template.keys():
                    print(">>Invalid input : try again")
                    self.disp_help_template()
                    ip = int(input(">>Please input the plot choice\n>>"))
                return plot_template[ip][1].split(':')

            def get_custom_config(self):
                ip = input(">>Please input the plot configuration => LogString1-item1,item2...:LogString2-item1,item2... \n>>")
                ip = ip.split(':')
                input(">>")
                return ip

            def get_cdf_config(self):
                ip = input(">>Please input the plot configuration => LogString1-item1 \n>>")
                ip = ip.split(':')
                return ip

            def get_input(self):
                cfglst = validate_input_args()
                self.filename = cfglst[0]
                self.plot_type = cfglst[1]
                self.isTemplated = cfglst[2]

                if self.plot_type == 1 and self.isTemplated == 1:
                    self.plot_config = self.get_templated_config()
                elif self.plot_type == 3 :
                    self.plot_config = self.get_cdf_config()
                else:
                    self.plot_config = self.get_custom_config()
                print(self.plot_config, self.plot_type)

        class Ue:
            ueid = None
            plotDict = {}

            def __init__(self, ueid, searchItems):
                self.ueid = ueid
                self.plotDict = {}
                for searchstring,plotStrings in searchItems.items():
                    for plotString in plotStrings:
                        self.plotDict[plotString] = {}

            def printData(self):
                for key,value in self.plotDict.items():
                    print(self.ueid,key,self.plotDict[key])

            def plot(self, plot_type):
                if plot_type==1:
                    xlabel = 'SFN'
                    ylabel = ''
                    for plotItem in self.plotDict.keys():
                        ylabel = ylabel + plotItem
                        title = str(self.ueid) + ' Time-Series'
                        x,y = zip(*sorted(self.plotDict[plotItem].items()))
                        chart_1 = get_plot(x, y, title,xlabel,ylabel)
                        chart.append(chart_1)
                        plt.legend()
                    plt.xlabel(xlabel)
                    plt.ylabel(ylabel)
                    plt.title(title)
                    plt.legend()
                elif plot_type==2:
                    tmp = list(self.plotDict.keys())
                    if len(tmp) != 2:
                        exit()
                    xlabel = tmp[0]
                    ylabel = tmp[1]
                    title = str(self.ueid) + ' : ' + xlabel + ' vs ' + ylabel
                    tmp = ((self.plotDict[xlabel][key],self.plotDict[ylabel][key]) for key in self.plotDict[xlabel].keys() if key in self.plotDict[ylabel].keys())
                    x,y = zip(*tmp)
                    #plt.scatter(x, y, label = title, linewidth = 2,marker = '.', markersize = 4)
                    plt.scatter(x, y, label = title, linewidth = 2)
                else:
                    tmp = list(self.plotDict.keys())
                    if len(tmp) != 1:
                        exit()
                    xlabel = tmp[0]
                    #x,y = zip(*sorted(self.plotDict[tmp[0]].items()))
                    x,y = zip(*(self.plotDict[tmp[0]].items()))
                    x=np.sort(y)
                    y = np.arange(0.0,len(x)+0.0)/len(x)
                    print(x,y)
                    # plt.plot(x,y,marker='.',linestyle='none')
                    chart_2 = get_plot(x,y,"NMK vs NNK", xlabel,'CDF')
                    chart.append(chart_2)
                    plt.xlabel(xlabel)
                    plt.ylabel('CDF')
                    plt.margins(0.02)

        class Graph:
            config = None
            uelst = []
            searchItems = {}
            ueDict = {}
            def __init__(self,gConfig):
                self.config = gConfig

            def Configure(self):
                for items in self.config.plot_config:
                    items = items.split("-")
                    if len(items) < 2:
                        print(">>Bad input format for log entries")
                        exit()
                    self.searchItems[items[0]] = []
                    tmpPlotItems = items[1].split(",")
                    for plotItem in tmpPlotItems:
                        self.searchItems[items[0]].append(plotItem)
                        # print(self.searchItems)


            def getUe(self,ueid):
                if ueid in self.ueDict.keys():
                    return self.ueDict[ueid]
                else:
                    newUe = Ue(ueid, self.searchItems)
                    self.ueDict[ueid] = newUe
                    return self.ueDict[ueid]

            def parseFile(self):
                with open(self.config.filename.read()) as src_file:
                    fileData = src_file.readlines()

                for currentLine in fileData:
                    for searchString in self.searchItems.keys():
                        if searchString in currentLine:
                            line = [x.strip(' ').strip('[') for x in currentLine.split(']')]
                            currentSfn = conv_sfn(datetime.strptime(line[0],'%d/%m/%Y %H:%M:%S.%f')) - start_time
                            line[-1:] = (line[5].strip('\n').split(':'))
                            if "UE_ID" in currentLine:
                                ueentry = currentLine.split("UE_ID:")[1].split(':')[0]
                                ueid = int(ueentry[-5:])
                                cellid = int(ueentry[-9:-7])
                            else:
                                ueid = 0
                                cellid = 0
                            currentUe = self.getUe(ueid)

                            for plotItem in self.searchItems[searchString]:
                                if(plotItem in line):
                                    plotData = getPlotData(line,plotItem)
                                    self.ueDict[ueid].plotDict[plotItem][currentSfn] = plotData

            def plot(self, ueid):
                if self.config.plot_type==1:
                    xlabel = 'SFN'
                    ylabel = ''
                    for plotItem in self.ueDict[ueid].plotDict.keys():
                        ylabel = ylabel + plotItem
                        title = str(ueid) + ' Time-Series'
                        x,y = zip(*sorted(self.ueDict[ueid].plotDict[plotItem].items()))
                        chart_3 = get_plot(x,y,"title","x","y")
                        chart.append(chart_3)
                        plt.legend()
                else:
                    tmp = list(self.plotDict.keys())
                    if len(tmp) != 2:
                        exit()
                    xlabel = tmp[0]
                    ylabel = tmp[1]
                    title = str(self.ueid) + ' : ' + xlabel + ' vs ' + ylabel
                    tmp = ((self.plotDict[xlabel][key],self.plotDict[ylabel][key]) for key in self.plotDict[xlabel].keys() if key in self.plotDict[ylabel].keys())
                    x,y = zip(*tmp)
                    #plt.scatter(x, y, label = title, linewidth = 2,marker = '.', markersize = 4)
                    plt.scatter(x, y, label = title, linewidth = 2)
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                plt.title(title)
                plt.legend()

            def printData(self):
                for ueid in self.ueDict.keys():
                    self.ueDict[ueid].printData()

            def plotData(self):
                ueid = get_ue_filter(self.ueDict.keys())
                print(ueid,"in Graph::plotData")
                if ueid == -1:
                    for ueid in self.ueDict.keys():
                        self.ueDict[ueid].plot(self.config.plot_type)
                        print("plotted")
                else:
                    self.ueDict[ueid].plot(self.config.plot_type)

        def getPlotData(line,plotItem):
            #Handle this special case due to log limitation
            if ('RB_PH_VAL_1000000_DERIVED_PH_VAL_1000_ALLOCATED' in line):
                index = line.index('RB_PH_VAL_1000000_DERIVED_PH_VAL_1000_ALLOCATED')
                val = int(line[index+1])
                line[index] = 'ALLOCATED_RB'
                line[index+1] = val%1000
                line.extend(('DERIVED_PH_VAL_RB',(val/1000) %1000))
                line.extend(('PH_VAL_RB', (val/1000000)%1000))
            index = line.index(plotItem)
            if '_100' in str(plotItem):
                return float(line[index+1])/100.0
            if '_10000' in str(plotItem):
                return float(line[index+1])/10000.0
            return int(line[index+1])


        def get_ue_filter(ueidLst):
            print("System Cell/UE details : ",ueidLst)
            ueid = input(">>Please enter the ueid for the plot\n>>")
            try:
                ueid = int(ueid)
            except ValueError as verr:
                ueid = -1
            if ueid not in ueidLst:
                print("Invalid input : Continuing with default")
                ueid = -1
            return ueid

        #Main
        config = validate_input_args()
        gPlotConfig = PlotConfig()
        # start_time = get_start_time(gPlotConfig.filename)
        graph = Graph(gPlotConfig)
        graph.Configure()
        graph.parseFile()
        # graph.printData()
        plt.ylim((-200,500))
        graph.plotData()
        # plt.show()
        # charts = [ chart_1, chart_2, chart_3]
        return render(request,'OTA_Algo_Pages/ota_algo_homepage.html', {'charts':chart})
            
                
