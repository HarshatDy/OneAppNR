from django.shortcuts import render,redirect
from Frequency_Tool_5G.utils import get_plot, get_single_plot, get_line, get_patch
from matplotlib import pyplot as plt, patches
# Create your views here.

def nr_arfcn_homepage(request):
    return render(request,"NR_ARFCN_GSCN_Pages/nr_arfcn_homepage.html")

def nr_arfcn_calculation(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('freq_homepage')
    else:
        global chart_1
        #########freqToArfcn###############
        def freqToArfcn(freq):
            arfcn_ = 0
            if freq < 3000000:
                arfcn_ = (freq - 0)/5 + 0                                                                                            
                                                                                                                                    
            elif(freq <= 24250000):                                                                                              
                arfcn_ = (freq - 3000000)/15 + 600000                                                                              

            elif (freq <= 100000000):                                                                                             
                arfcn_ = (freq - 24250080)/60 + 2016667                                                                                                                                                                                                                                                                                                                                                                                                                  
            
            return arfcn_
        ###########################End of FreqToArfcn function###########################

        #########arfcnToFreq##############
        def arfcnToFreq(arfcn):
            freq_ = 0;                                                                                                                                                                                                                                

            if (arfcn <= 599999):                                                                                                            
                freq_ = 0 + 5 * (arfcn - 0)

            elif(arfcn <= 2016666):                                                                                                                                                                                                                    
                freq_ = 3000000 + 15 * (arfcn - 600000)

            elif (arfcn <= 3279165):                                                                                                                                                                                                                    
                freq_ = 24250080 + 60 * (arfcn - 2016667) 

            return freq_
        ###########################End of arfcnToFreq function###########################

        #########prb_calculation###########
        #Enter Bandwidth, Subcarrier spacing and Numerology to calculate PRB
        def prb_calculation(bwd_, scs_, nrMU_):

            guard_data = [[5, 10, 15, 20, 25, 30, 40, 50, 60, 80, 90, 100],
                        [242.5, 312.5, 382.5, 452.5, 522.5, 592.5, 552.5, 692.5, 0, 0, 0, 0],
                        [505, 665, 645, 805, 785, 945, 905, 1045, 825, 925, 885, 845],
                        [0, 1010, 990, 1330, 1310, 1290, 1610, 1570, 1530, 1450, 1410, 1370]]

            guard_band = 0.0
            row = 1
            if (scs_ == 15):
                row = 1
            elif (scs_ == 30):
                row = 2
            elif (scs_ == 60):
                row = 3
            found = False

            for col in range(12):
                if (guard_data[0][col]==bwd_) and (guard_data[0][col] != 0) :
                    found = True
                    guard_band = float(guard_data[row][col])
                    print("gaurdband = ")
                    print(guard_band)
                    break
                else:
                    found = False
            if(found == False):
                return -1

            ##One resource block in a perticuler numerology
            rb_ = 0
            if nrMU_ == 0: #mu0
                rb_ = 180
            elif nrMU_ == 1:  #mu1
                rb_ = 360
            elif nrMU_ == 2:  #mu2
                rb_ = 720

            ## #of PRB = (Bandwidth * 10^3 - 2 * gurdband) / rb_
            noOfRB = (int(bwd_) * 1000 - 2 * int(guard_band)) / rb_
            print("no of tot RBs")
            print(int(noOfRB))
            return int(noOfRB)
        #####################End of prb_calculation function##########################

        carrBand_ = request.POST.get("carrierband")
        carrBand = int(carrBand_)
        scS_ = request.POST.get("scs")
        scs = int(scS_)
        nrMu_ = request.POST.get("nrmu")
        nrMU = int(nrMu_)
        bwdl_ = request.POST.get("bwdl")
        bwDL = int(bwdl_)
        freq_range = request.POST.get("fr")
        scsb_crb = 15

        absFreqssb_ = request.POST.get("absfreqssb")
        absFreqSsb = int(absFreqssb_)

        dlEarfcN_ = request.POST.get("dlearfcn")
        dlEarfcn = int(dlEarfcN_)
        if(freq_range =='FR2'):
            scsb_crb = 60

        #absFreqPointA = 3700560
        #absArfcnPointA = 646704

        #absArfcnSsb = 647232
        #dlEarfcn = 649980
        print("arfcnToFreq(dlEarfcn)")
        print(arfcnToFreq(dlEarfcn))

        totPRB = prb_calculation(bwDL, scs, nrMU)
        print("Total PRB calculated:" + str(totPRB))

        absFreqPointA = arfcnToFreq(dlEarfcn) - ((totPRB) * scs * 12) / 2
        print(absFreqPointA)

        absFreqofSsbRb0 = absFreqSsb - 10 * 12 * scs

        if(absFreqofSsbRb0 < absFreqPointA):
            print("INVALID absFreqofSsbRb0 as it is less than absFreqPointA")
            return render(request,"NR_ARFCN_GSCN_Pages/nr_arfcn_homepage.html")
        else:
            offsetToPointA = (absFreqSsb - absFreqPointA - (10 * 12 * scs)) / (12 * scsb_crb)
            print (offsetToPointA)

            fig, ax = plt.subplots()
            ax.axis([0, 10 , 0, totPRB])
            ax.locator_params('y', nbins=20)
            ax.locator_params('x', nbins=10)
            
            ax.set_ylabel('PRB->')
            ax.set_xlabel('Time slot->')
            #ax.plot([0, 10],[0, totPRB])
            ssb_plot = patches.Rectangle((1, offsetToPointA), 1, offsetToPointA+20, edgecolor='black',
            facecolor="yellow", linewidth=1)
            
            
            sss_plot = patches.Rectangle((1.2, offsetToPointA + 5), 0.6, offsetToPointA+10, edgecolor='black',
            facecolor="green", linewidth=1)
            rx, ry = sss_plot.get_xy()
            cx = rx + sss_plot.get_width()/2.0
            cy = ry + sss_plot.get_height()/2.0
            ax.annotate("SSB", (cx, cy), color='black', weight='bold', fontsize=6, ha='center', va='center')
            ax.annotate("<-offsetToPointA = " + str(int(offsetToPointA)), (3, offsetToPointA - 2), color='black', weight='bold', fontsize=5, ha='center', va='bottom')
            ax.annotate("<-absFreqofSsbRb0 = " + str(int(absFreqofSsbRb0)), (5.5, absFreqofSsbRb0 - 5), color='black', weight='bold', fontsize=5, ha='center', va='bottom')


            # ax.add_patch(ssb_plot)
            # ax.add_patch(sss_plot)

            # chart_1 = ax.to_html()
            chart_1 = get_patch(ax,ssb_plot,sss_plot)
            #ax.add_patch(Rectangle((1, offsetToPointA), 2, offsetToPointA+20))
            
            #display plot
            # plt.show()
            return render(request,"NR_ARFCN_GSCN_Pages/nr_arfcn_homepage.html", {"charts":chart_1})