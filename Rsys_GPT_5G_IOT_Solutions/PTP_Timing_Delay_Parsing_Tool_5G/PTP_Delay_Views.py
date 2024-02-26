from calendar import c
from django.shortcuts import render ,redirect
import re
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
import pandas as pd
import sys
import os
import glob
import numpy as np
from Frequency_Tool_5G.utils import get_plot, get_single_plot
import matplotlib.pyplot as plt
import matplotlib
from django_matplotlib.fields import MatplotlibFigureField

import plotly.express as px

def ptp_delay_homepage(request):
    return render(request,"PTP_Timing_Delay_Pages/ptp_timing_homepage.html")


def ptp_delay_calculation(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('freq_homepage')
    elif request.FILES.get('ptp_log_file') and request.FILES.get('phc_log_file'):
        phc_log_file = request.FILES['phc_log_file']
        ptp_log_file= request.FILES['ptp_log_file']
        matplotlib.use('Agg')
        class ptpParser:
            def __init__(self):
                self.rptp = re.compile(r'(?=ptp4l).+?\[(\d+\.\d+)\]:\s(?:master offset).+?([-+]\d+).+?(?:s)(\d+)\s(?:freq).+?([-+]\d+)\s(?:path delay).+?(\d+)$', re.MULTILINE)
                self.rphc2sys = re.compile(r'(?=phc2sys).+?\[(\d+\.\d+)\]:\s(?:CLOCK_REALTIME phc offset).+?(\d+).+?(?:s)(\d)\s(?:freq).+?([-+]\d+)\s(?:delay).+?(\d+)$', re.MULTILINE)
                self.pathname = sys.argv[1]

            def ptp4l(self, filename):
                return np.fromregex(filename, self.rptp, [('kernelTime', np.float32), ('masterOffset', np.int64), ('state', np.int8), ('freq', np.int64), ('pathDelay', np.int64)], encoding='UTF-8')

            def phc2sys(self, filename):
                return np.fromregex(filename, self.rphc2sys, [('kernelTime', np.float32), ('phcOffset', np.int64), ('state', np.int8), ('freq', np.int64), ('Delay', np.int64)], encoding='UTF-8')

            def getData(self):
                for file in glob.iglob(f'{self.pathname}/*.log'):
                    # sys.stdout.write(f'processing filename {os.path.basename(file)}\n')
                    if os.path.basename(file) == 'ptp4l_log.log':
                        data = pd.DataFrame(self.ptp4l(file))
                        data.to_csv(os.path.basename(file) + '.csv', index=False)
                    elif os.path.basename(file) == 'phc2sys_log.log':
                        data = pd.DataFrame(self.phc2sys(file))
                        data.to_csv(os.path.basename(file) + '.csv', index=False)
                    else:
                        sys.stderr.write('invalid file !!!\n')
                        break
                return None

        if __name__ == ('__main__'):
            parser = ptpParser()
            parser.getData()

        global chart_1, chart_2
        # Set the figure size
        plt.rcParams["figure.figsize"] = [7.00, 3.50]
        plt.rcParams["figure.autolayout"] = True
        # Make a list of columns
        columns = ['kernelTime', 'masterOffset','state','pathDelay']
        #columns = ['timestamp', 'DL_BLER%', 'DL_AVG_MCS','UL_AvgPHY_THPT_KBPS','UL_BLER','UL_AvgMCS']
        #'DL_AvgPHY_THPT_KBPS'
        # Read a CSV file
        df = pd.read_csv(ptp_log_file, usecols=columns)
        # Plot the lines
        chart_1 = get_single_plot(df, 'unk','x')
        # plt.show()

        plt.rcParams["figure.figsize"] = [7.00, 3.50]
        plt.rcParams["figure.autolayout"] = True
        # Make a list of columns
        columns = ['kernelTime', 'phcOffset','state','Delay']
        #columns = ['timestamp', 'DL_BLER%', 'DL_AVG_MCS','UL_AvgPHY_THPT_KBPS','UL_BLER','UL_AvgMCS']
        #'DL_AvgPHY_THPT_KBPS'
        # Read a CSV file
        df = pd.read_csv(phc_log_file, usecols=columns)
        # Plot the lines
        chart_2 = get_single_plot(df,'UNK','X')
        # df.plot()
        # plt.show()

        charts = [ chart_1, chart_2]

        return render(request,'PTP_Timing_Delay_Pages/ptp_timing_homepage.html', {'charts':charts})
            
                
