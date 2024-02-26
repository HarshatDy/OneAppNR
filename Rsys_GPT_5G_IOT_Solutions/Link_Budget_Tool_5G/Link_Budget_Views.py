import math
from django.shortcuts import render, redirect
import matplotlib.pyplot as plt

from Frequency_Tool_5G.utils import get_graph, get_plot, get_bar

def link_budget_homepage(request):
    return render(request,"Link_Budget_Pages/link_budget_homepage.html")

def link_budget_calculation(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('freq_homepage')
    else:
        
        #gNodeB transmit power (dBm)
        gTransPow = float(request.POST.get('gtranspow'))

        #subcarrier quantity
        # subCarrierQty = float(request.POST.get('subcarrierqty'))

        #gNodeB antenna gain (dBi)
        gAntGain =float(request.POST.get('gantgain'))

        #gNodeB cable loss (dB)
        gCableLoss = float(request.POST.get('gcableloss'))

        #Path loss(dB) --- to be worked
        PathLoss =float(request.POST.get('pathloss'))

        #Penetration loss(dB)
        PenetLoss = float(request.POST.get('penetloss'))

        #foliage loss (dB)
        FoliageLoss = float(request.POST.get('foliageloss'))

        #body block loss (dB)
        BodyBockLoss = float(request.POST.get('bodybockloss'))

        #interference margin (dB)
        InterferMargin = float(request.POST.get('interfermargin'))

        #rain/ice margin (dB)
        RainIceMargin = float(request.POST.get('rainicemargin'))

        #Slow Fading margin (dB)
        SlowFadingMargin = float(request.POST.get('slowfadingmargin'))

        #UE antenna gain (dB)
        UEAntGain = float(request.POST.get('ueantgain'))

        UECableLoss = float(request.POST.get('uecableloss'))

        Received_Signal_level_at_rcvr = gTransPow + gAntGain - gCableLoss + UEAntGain - UECableLoss - PathLoss -  PenetLoss - FoliageLoss - BodyBockLoss - InterferMargin - RainIceMargin - SlowFadingMargin 

        print ('Received Signal level at receiver',Received_Signal_level_at_rcvr)

        #Calculation of Receiver sensitivity [Receiver sensitivity (dBm) = Noise figure (dB) + Thermal Noise (dBm) + SINR (dB)]

        #Noise figure (dB)
        NoiseFig = float(request.POST.get('noisefig'))

        #Thermal Noise (dBm)
        ThermalNoise = float(request.POST.get('thermalnoise'))

        #demodulation threshold SINR (dB)
        thresholdSINR = float(request.POST.get('thresholdsinr'))

        Receiver_Sensitivity = NoiseFig + ThermalNoise + thresholdSINR

        print ('Receiver Sentivity is',Receiver_Sensitivity)

        if (Received_Signal_level_at_rcvr > Receiver_Sensitivity):
            xlabel = 'Radio Channel Status : PASS'
        else:
            xlabel = 'Radio Channel Status : FAIL'

        #plotting receiver power and receiver sensitivity graph 


        x1 = ['receiver_power','receiver_sensitivity']
        y1 = [Received_Signal_level_at_rcvr,Receiver_Sensitivity]

        # plt.ylabel('Units in dBm')
        ylabel = "Units in dBm"

        # giving a title to my graph
        # plt.title('Link Budget Calculator!!! ')


        # plotting values 
        # chart =get_plot(x1,y1,'Link Budget Calculator!!! ','x','y')
        # plt.bar(x1, y1, color = 'lightgrey', edgecolor='blue')
        # chart = get_graph()
        charts = get_bar(x1, y1,'Link Budget Calculator',xlabel,ylabel,'lightgrey','blue')
            
        # show a legend on the plot
        # plt.legend()
        
        # function to show the plot
        # plt.show()

        return render(request,"Link_Budget_Pages/link_budget_homepage.html",{'charts':charts})