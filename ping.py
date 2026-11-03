from scapy.all import IP ,ICMP,sr1
from art import text2art
from pystyle import Colors,Write
import time
#packet crafting
print(text2art('ping tool'))
input("Please tape enter  to pass :")
with open ("Data.txt","r") as f:
    for line in f:
        target=line.strip()
        packet=IP(dst=target)/ICMP()
        start_time=time.time()
        reply = sr1(packet, timeout=2, verbose=False)
        end_time=time.time()

#condition

        if reply:
             duration=(end_time-start_time)*1000
             print(reply.ttl)
             ttl = int(reply.ttl)
             Write.Print("Mybe os is : ",Colors.blue_to_cyan)
             print("Linux" if ttl<=64 else "Windows" if ttl<=128 else "Cisco" if ttl<=255 else "Unknown")
        else:
             Write.Print("we have problem mybe is firewalle or else problem  ",Colors.black_to_red)