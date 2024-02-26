#Author @Shantnu Singh
import math


from django.shortcuts import render ,redirect
import re
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages

def pathloss_homepage(request):
    return render(request,"NR_Free_Space_Path_Loss_Pages/pathloss.html")


def calculate_fspl(distance, frequency):
#     # Check if the inputs are valid
#     if distance <= 0:
#         raise ValueError("Distance must be greater than zero.")
#     if frequency <= 0:
#         raise ValueError("Frequency must be greater than zero.")

#     # Convert the frequency to MHz
#     frequency_mhz = frequency * 10**6

#     # Calculate the FSPL in decibels (dB)
#     fspl_db = 20 * math.log10(distance) + 20 * math.log10(frequency_mhz) + 20 * math.log10(4 * math.pi / 299792458)

#     return fspl_db

# # Example usage:
# try:
#     distance_km = float(input("Enter the distance between the transmitter and receiver in kilometers: "))
#     frequency_ghz = float(input("Enter the frequency of the signal in GHz: "))

#     fspl_result = calculate_fspl(distance_km * 1000, frequency_ghz)
#     print(f"Free Space Path Loss (FSPL) in dB: {fspl_result} dB")

# except ValueError as e:
#     print(str(e))
# except Exception as e:
#     print("An error occurred:", str(e))
    return 0