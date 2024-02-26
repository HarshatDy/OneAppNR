from django.shortcuts import render ,redirect
import re
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages

from Frequency_Tool_5G.utils import get_plot, get_single_plot, get_line
# import matplotlib.pyplot as plt
import matplotlib

import re
import numpy as np
import pandas as pd
import sys
import glob
import os
import matplotlib.pyplot as plt
from configparser import ConfigParser
import plotly.express as px


import plotly.express as px

def qual_log_homepage(request):
    return render(request,"Qual_Log_Parsing_Pages/qual_log_homepage.html")



def qual_log_calculation(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('Qual_Log_Parsing_Pages/qual_log_homepage.html')
    elif request.FILES.get('qual_log_file'):
        qual_log_file= request.FILES['qual_log_file']
        matplotlib.use('Agg')
        global chart
        class qcatStatParser:
            def __init__(self):
                self.config = ConfigParser()
                self.config.read('config.ini')
                self.path = self.config['DEFAULT']['stats_path']
                self.setup = self.config['DEFAULT']['setup_name']
                if self.config.has_option('DEFAULT','csv_save_to_dir'):
                    self.csv_out_path = self.config['DEFAULT']['csv_save_to_dir']
                else:
                    self.csv_out_path = False
                sys.stdout.write(f'output path is {self.csv_out_path}\n')
                self.cell = None

        def get_dl_q_thpt_stats(self, filename):
            qreg = "(?:QTRACE)\s(?P<timestamp>\d{1,2}:\d{1,2}:\d{1,2}\.\d{1,})(?:.+?\|\sDL.+?AvgPHY:\s)(?P<AvgPHY_THPT_KBPS>\d{1,})(?:.+?BLER:\s{1,2})(?P<BLER>\d{1,})(?:.+?#\s)(?P<CRC_PASS>\d{1,})\/(?P<CRC_FAIL>\d{1,})(?:.+?AvgTB:\s)(?P<AVG_TB_BYTES>\d{1,})(?:.+?AvgMCS:\s)(?P<AVG_MCS>\d{1,})(?:.+?AvgRB:\s)(?P<AVG_RB>\d{1,})(?:.+?#\s)(?P<HARQ_FAIL>\d{1,})\/(?P<HARQ_RECOVERY>\d{1,})\/(?P<HARQ_REDUNDANT>\d{1,})"
            return np.fromregex(filename, qreg, [("timestamp", np.unicode_, 32), ("DL_AvgPHY_THPT_KBPS", np.int), ("DL_BLER%", np.int), ("DL_CRC_PASS%", np.int), ("DL_CRC_FAIL%", np.int), ("DL_AVG_TB_BYTES", np.int), ("DL_AVG_MCS", np.int), ("DL_AVG_RB", np.int), ("DL_HARQ_FAIL", np.int), ("DL_HARQ_RECOVERY", np.int), ("DL_HARQ_REDUNDANT", np.int)])

        def get_ul_q_thpt_stats(self, filename):
            qreg = "(?:QTRACE)\s(?:.+?\|\sUL.+?AvgPHY:\s+?)(?P<AvgPHY_THPT_KBPS>\d{1,})(?:.+?BLER:.+?)(?P<BLER>\d{1,})(?:.+?#\s)(?P<CRC_FAIL>\d{1,})(?:.+?TXcnt:\s)(?P<TXcnt>\d{1,})(?:.+?AvgTB:\s)(?P<AvgTB_BYTES>\d{1,})(?:.+?AvgMCS:\s)(?P<AvgMCS>\d{1,})(?:.+?AvgRB:\s)(?P<AvgRB>\d{1,})(?:.+?AvgLayers\*10:\s)(?P<AvgLayers>\d{1,})(?:.+?AvgRank\*10:\s)(?P<AvgRank>\d{1,})(?:.+?AvgPHRidx:\s)(?P<AvgPHRidx>\d{1,})"
            return np.fromregex(filename, qreg, [("UL_AvgPHY_THPT_KBPS", np.int), ("UL_BLER", np.int), ("UL_CRC_FAIL", np.int), ("UL_TXcnt", np.int), ("UL_AvgTB_BYTES", np.int), ("UL_AvgMCS", np.int), ("UL_AvgRB", np.int), ("UL_AvgLayers*10",np.int), ("UL_AvgRank*10", np.int), ("UL_AvgPHRidx", np.int)])


        def get_csv(self):
            data = []
            # sys.stdout.write(f'started processing file from path {path}\n')
            for file in glob.iglob(f'{self.path}/*.txt*'):
                sys.stdout.write(f'processing {file} in dir ' + os.path.basename(self.path) + '\n')
                data.append(pd.concat([pd.DataFrame(self.get_dl_q_thpt_stats(file)), pd.DataFrame(self.get_ul_q_thpt_stats(file))], axis = 1))
            # print(data)
            data = pd.concat(data)
            # data = data.T.drop_duplicates().T
            name = os.path.basename(file).rsplit('.txt', 1)
            return data.to_csv(self.setup + '_' + name[0] + '.csv', index=False) if self.csv_out_path == False else data.to_csv(self.csv_out_path +  self.setup + '_' + name[0] + '.csv', index=False), sys.stdout.write(f'processed output file at {os.path.dirname(os.path.abspath(sys.argv[0]))}\n') if self.csv_out_path == False else sys.stdout.write(f'processed file at {self.csv_out_path}\n')


        if __name__ == ('__main__'):
            qcat_parser = qcatStatParser()
            qcat_parser.get_csv()

        df = pd.read_csv(qual_log_file)
        df.head()
        # fig = px.line(df, x = 'timestamp', y = 'DL_AvgPHY_THPT_KBPS', title='QXDM BLER - Throughput Plot')
        chart_ply = get_line(df,'QXDM BLER - Throughput Plot','DL_AvgPHY_THPT_KBPS','timestamp')
        chart = chart_ply.to_html(full_html=False, default_height=500, default_width=700)
        # chart = chart_ply.to_image(format='png')
        # print(chart)
        return render(request,"Qual_Log_Parsing_Pages/qual_log_homepage.html",{'charts':chart})

    