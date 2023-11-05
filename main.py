import psutil
from scapy.all import *

addrs = psutil.net_if_addrs()
NICs = addrs.keys()
NICsList = list(NICs)

def choiceMaker(count, start=0, prompt="Enter your selection"):
    print(prompt)
    try:
        choice = int(input(prompt))
    except ValueError:
        print("Error: An integer (whole number) must be entered to make a selection")
        return False

    if choice > (start + count) or choice < start:
        print("Error: Selection out of bounds")
        return False

    return choice

def selectNIC(list):
    print("Select Network Interface Card")
    for i in range(len(list)):
        print(f"{i}: {list[i]}")
    selectionMade = False
    while not selectionMade:
        try:
            choice = choiceMaker(count=len(NICsList), prompt="Enter a number for a Network Card: ")
            selectionMade = True
        except ValueError:
            selectionMade = False
    return list[choice]
def sniffInterface(interface):
    print("====================================================")
    print(f"\nSniffing interface: {interface}")
    sniff(iface=interface, prn=lambda x:x.show(), count=1)

# print (NICsList)
sniffInterface(selectNIC(NICsList))

