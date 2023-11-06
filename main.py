import psutil
from scapy.all import *

addrs = psutil.net_if_addrs()
NICs = addrs.keys()
NICsList = list(NICs)

runSniff = False

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
    sniff(iface=interface, prn=lambda x:x.summary(), stop_filter=stopSniff)

def stopSniff(x):
    # print("This is the variable from stop_filter " + x)
    return not runSniff

class ScreenBuffer:
    o_buffer = []
    
    @classmethod
    def buff(cls, input):
        cls.o_buffer.append(input)

    @classmethod    
    def buffl(cls, input):
        cls.o_buffer.append(input+"\n")

    @classmethod
    def render(cls):
        output = ""
        for line in cls.o_buffer:
            output+=line
        print(output)


# print (NICsList)

sb = ScreenBuffer
sb.buff("This is bread")
sb.buffl("This is bread that makes a new line")
sb.render()

NICChoice = selectNIC(NICsList)
runSniff = True
threading.Thread(target=lambda: sniffInterface(NICChoice)).start()

exit = False
input("Press enter to stop sniffing")
runSniff=False



