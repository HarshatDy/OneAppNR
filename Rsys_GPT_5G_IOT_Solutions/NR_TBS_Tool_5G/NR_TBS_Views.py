#Author @Shantnu Singh
import math


from django.shortcuts import render ,redirect
import re
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages

def tbs_homepage(request):
    return render(request,"NR_TBS_Pages/tbs.html")


def calculate_tbs(mcs_index, num_rb, num_tx_antennas):
#     if not (0 <= mcs_index <= 27) or num_rb <= 0 or num_tx_antennas <= 0:
#         raise ValueError("Invalid MCS index, number of resource blocks, or number of transmit antennas.")

#     # Calculate the TBS using the formula specified in the 3GPP specification
#     R = num_rb
#     Qm = 2  # QPSK modulation for all MCS indices in the range [0, 27]

#     if mcs_index <= 9:
#         C = 1
#     elif mcs_index <= 15:
#         C = 2
#     else:
#         C = 3

#     Ninfo = (156 * R) - 16

#     tbs = (math.floor((Ninfo - 24 * C) / (Qm * C))) * C

#     # Apply antenna ports correction
#     if num_tx_antennas == 1:
#         tbs = max(tbs, 0)
#     else:
#         tbs = max(tbs, 2)

#     return tbs

# # Example usage:
# try:
#     mcs_index = int(input("Enter the MCS index (0-27): "))
#     num_rb = int(input("Enter the number of resource blocks: "))
#     num_tx_antennas = int(input("Enter the number of transmit antennas (1 or 2): "))

#     tbs_result = calculate_tbs(mcs_index, num_rb, num_tx_antennas)
#     print(f"TBS for MCS index {mcs_index}, {num_rb} resource blocks, and {num_tx_antennas} transmit antennas: {tbs_result} bits")

# except ValueError as e:
#     print(str(e))
# except Exception as e:
#     print("An error occurred:", str(e))
    return 0