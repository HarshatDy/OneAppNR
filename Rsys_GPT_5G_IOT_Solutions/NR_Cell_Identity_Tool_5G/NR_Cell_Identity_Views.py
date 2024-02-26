#Author @Shantnu Singh

from django.shortcuts import render ,redirect
import re
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages

def cell_identity_homepage(request):
    return render(request,"NR_Cell_Identity_Pages/cell_identity.html")


def calculate_nci(pci, c_rnti):
#     # Check if the inputs are within valid ranges
#     if not (0 <= pci <= 0xFFFFF):
#         raise ValueError("PCI value must be between 0 and 0xFFFFF (20 bits).")
#     if not (0 <= c_rnti <= 0xFFFF):
#         raise ValueError("C-RNTI value must be between 0 and 0xFFFF (16 bits).")

#     # Shift the PCI to the upper 20 bits and combine it with the C-RNTI in the lower 16 bits
#     nci = (pci << 16) | c_rnti
#     return nci

# # Example usage:
# try:
#     pci_value = int(input("Enter the Physical Cell Identity (PCI) value (0 to 1048575): "))
#     crnti_value = int(input("Enter the Cell Radio Network Temporary Identifier (C-RNTI) value (0 to 65535): "))

#     nci_result = calculate_nci(pci_value, crnti_value)
#     print(f"5G NR Cell Identity (NCI): {nci_result}")

# except ValueError as e:
#     print(str(e))
# except Exception as e:
#     print("An error occurred:", str(e))
    return 0