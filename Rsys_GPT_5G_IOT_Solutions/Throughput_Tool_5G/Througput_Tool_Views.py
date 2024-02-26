import matplotlib.pyplot as plt
import plotly.graph_objects as go
import math
from django.contrib import messages



from django.shortcuts import render, redirect

def throughput_homepage(request):
    return render(request, 'Throughput_Tool_Pages/throughput_homepage.html')


def throughput_calculation(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('freq_homepage')
    elif request.POST:
        # du_log_file= request.FILES['du_log_file']
        # du_log_text = du_log_file.read().decode('utf-8')
        bandwidth = request.POST.get("bandwidth")
        # input1=input("Enter the 5G Channel Bandwidth (MHz): ")

        scs = request.POST.get("scs")
        # input2=input("Enter the Subcarrier spaching (KHZ) : ")

        mimo = request.POST.get("mimo")
        # MimoLayers=input("Enter the number of MIMO Layers (1 to 4) : " )

        mcscqi = request.POST.get("mcs")
        # Choice=input("Choose Input - 0 for CQI & 1 for MCS : " )

        mcscqivalue= request.POST.get("mcsvalue")
        # Index=input("Enter the correcpoding CQI(0-15) or MCS Index(0-27) : ")

        bler = request.POST.get("bler")
        # BlerTarget=input("Enter the block Error Rate (Percentage) : " )
        Throughput=[]

        x= int(bandwidth) * 1000 / int(scs) / 12

        NumPRBs= x - 4
        NumPRBs = math.floor(NumPRBs)
        print("Available number of PRBs is : "+str(NumPRBs))
        Dlslots = 1600
        SpecEffMcs=[0.2344, 0.3770, 0.6016,0.8770,  1.17758, 1.4766, 1.6953, 1.9141 , 2.1602, 2.4063, 2.5703, 2.7305, 3.0293, 3.3223, 3.6094, 3.9023 , 4.2129 , 4.5234, 4.8164, 5.1152, 5.332, 5.5547, 5.8906, 6.2266, 6.5703, 6.9141, 7.1602, 7.4063]
        SpecEffCqi=[0.1523,0.1523,0.377,0.877,1.4766,1.9141,2.4063,2.7305,3.3223,3.9023,4.5234,5.1152,5.5547,6.2266,6.9141,7.4063]
        if int(mcscqi)==0:
            y=SpecEffCqi[int(mcscqivalue)]
        elif  int(mcscqi)==1:
            y=SpecEffMcs[int(mcscqivalue)]


        #print("The MCS Spectral Efficiency is " + str(y))
        TbSize =132 * y
        TbSize = math.floor(TbSize)

        Throughput = int(TbSize) * int(NumPRBs) * int(Dlslots) * int(mimo) * ((100 - int(bler))/100)  /1000 /1000
        print("Maximum Throughput for this configuration is  : " + str(Throughput))
        #fig = go.Figure(go.Indicator(
        #   mode = "gauge +number",
        #   value = Throughput,
        #   title = {'text': 'Radisys gNB Peak 5G-Speed'}
        # ))
        #fig.show()
        #fig = go.Figure(go.Indicator(
        #    domain = {'x': [0, 1], 'y': [0, 1]},
        #    value = Throughput,
        #    mode = "gauge+number+delta",
        #    title = {'text': "Radisys 5G_gNB Peak Throughput "},
        #    delta = {'reference': 1707},
        #    gauge = {'axis': {'range': [None, 500]},
        #             'steps' : [
        #                 {'range': [0, 250], 'color': "lightgray"},
        #                 {'range': [250, 400], 'color': "gray"}],
        #             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

        #fig.show()

        fig = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = Throughput,
            domain = {'x': [0, 1], 'y': [0, 1]},
            #title = {'text': "RadiSys 5G-gNB Estimated Throughput", 'font': {'size': 40}},
            title = {'text': "RadiSys 5GNR gNodeB Estimated Throughput", 'font': {'size': 40, 'color':"Red"}},
            delta = {'reference': 1707, 'increasing': {'color': "RebeccaPurple"}},
            gauge = {
                'axis': {'range': [None, 1800], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "darkblue"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 400], 'color': 'cyan'},
                    {'range': [400, 1000], 'color': 'royalblue'},
                    {'range': [1000, 1800], 'color': 'green'}],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 1800}}))

        fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})
        chart =fig.to_html(full_html=False, default_height='100%', default_width='100%')
        print(chart)
        # fig.show()
        return render(request, 'Throughput_Tool_Pages/throughput_homepage.html',{'charts':chart})
