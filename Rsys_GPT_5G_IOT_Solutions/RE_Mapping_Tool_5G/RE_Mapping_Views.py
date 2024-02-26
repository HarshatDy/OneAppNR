from django.shortcuts import render, redirect
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
# include scipy's signal processing functions
import scipy.signal as signal
from scipy.fftpack import fft

from django.contrib import messages
from Frequency_Tool_5G.utils import get_plot, get_single_plot,get_scatter


def re_mapping_homepage(request):
    return render(request, 'RE_Mapping_Pages/re_mapping_homepage.html')

def re_mapping_calculation(request):
        # -*- coding: utf-8 -*-
    # includes core parts of numpy, matplotlib
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('Homepage')
    elif request.FILES.get('re_map_file'):
        re_map_file= request.FILES['re_map_file']
        dat = np.fromfile(re_map_file, dtype="int16")
        cplx = np.vectorize(complex)(dat[0::2], dat[1::2])
        # np.savetxt(r'C:\Atom-Python\RE-Mapping\newiq\iq_dl_ant0_car0.txt', cplx, fmt='%d')
        dat_cplx = dat.astype(np.float32).view(np.complex64)
        # plt.specgram(dat[0:3276*13])
        # plt.title("PSD of 'signal' loaded from file")
        # plt.xlabel("Time")
        # plt.ylabel("Frequency")
        # plt.show()
        # plt.psd(dat[26208:29484], Fs=30000*12*273, scale_by_freq=True, window=mlab.window_none)
        # plt.title("PSD of 'signal' loaded from file")
        # NFFT=len(dat_cplx[3276*2:3276*3:2]) #NFFT-point DFT
        # X=fft(dat_cplx,NFFT) #compute DFT using FFT
        # fig3, ax = plt.subplots(nrows=1, ncols=1) #create figure handle
        # fVals=np.arange(start = 0,stop = NFFT)/NFFT #DFT Sample points
        # ax.plot(fVals,np.abs(dat_cplx[3276*2:3276*3:2]))
        # ax.set_title('Double Sided FFT - with FFTShift')
        # ax.set_xlabel('Normalized Frequency')
        # ax.set_ylabel('DFT Values');
        # ax.autoscale(enable=True, axis='x', tight=True)
        # ax.set_xticks(np.arange(-0.5, 0.5+0.1,0.1))
        # fig3.show()
        NFFT=len(dat_cplx[3276*2:3276*3:2]) #NFFT-point DFT
        #X=fft(dat_cplx[0:3276],NFFT) #compute DFT using FFT
        fVals=np.arange(start = 0,stop = NFFT) #DFT Sample points
        # plt.plot(fVals, np.abs(dat_cplx[0:3276]))
        chart_1 = get_plot(fVals, np.abs(dat_cplx[3276*2:3276*3:2]), "UK vs UK","UKA","AKA")
        # plt.show()  
        chart_2 = get_plot(np.real(dat_cplx[3276*2:3276*3:2]), np.imag(dat_cplx[3276*2:3276*3:2]),"UNK vs UNK2", "UNK", "UNK2")
        chart_2 =get_scatter(np.real(dat_cplx[3276*2:3276*3:2]), np.imag(dat_cplx[3276*2:3276*3:2]),"UNK VS UNK2")
        # plt.title("Constellation of the 'signal' loaded from file")
        # plt.show()
        # plt.polar(np.real(dat[0:3276*14]), np.imag(dat[0:3276*14]))
        # plt.show()
        charts = [chart_1,chart_2]
        return render(request,'RE_Mapping_Pages/re_mapping_homepage.html', {'charts':charts})