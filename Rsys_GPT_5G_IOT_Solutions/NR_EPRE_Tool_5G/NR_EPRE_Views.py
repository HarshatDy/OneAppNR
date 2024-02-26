#@author Shantnu Singh

import math


from django.shortcuts import render ,redirect
import re
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages

def epre_homepage(request):
    return render(request,"NR_EPRE_Pages/epre.html")


def calculate_epre_power(output_power_per_tx_dBm, num_rb_per_cell):
#     epre_power_dBm = output_power_per_tx_dBm - 10 * math.log10(num_rb_per_cell * 12)
#     return epre_power_dBm

# # Take user input for Output Power per TX and Number of RB per Cell
# try:
#     output_power_per_tx_dBm = float(input("Enter the Output Power per TX in dBm: "))
#     num_rb_per_cell = int(input("Enter the Number of RB per Cell: "))

#     epre_power_dBm = calculate_epre_power(output_power_per_tx_dBm, num_rb_per_cell)
#     print(f"EPRE Power: {epre_power_dBm:.2f} dBm")

# except ValueError:
#     print("Invalid input. Please enter numeric values for both Output Power per TX and Number of RB per Cell.")
    return 0