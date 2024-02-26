#Author @Shantnu Singh


from django.shortcuts import render ,redirect
import re
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages

def ta_homepage(request):
    return render(request,"NR_TA_Pages/ta.html")


def calculate_5g_timing_advance_distance(timing_advance, sampling_rate=30.72e6):
#     speed_of_light = 3.00e8  # Speed of light in meters per second
#     timing_advance_distance = (timing_advance * speed_of_light) / (2 * sampling_rate)
#     return timing_advance_distance

# # Example usage:
# try:
#     timing_advance_value = int(input("Enter the Timing Advance value (in symbols): "))
#     timing_advance_distance_meters = calculate_5g_timing_advance_distance(timing_advance_value)
#     print(f"Timing Advance Distance: {timing_advance_distance_meters:.2f} meters")

# except ValueError:
#     print("Invalid input. Please enter an integer value for the Timing Advance.")
    return 0