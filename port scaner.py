import socket
from pystyle import Colors,Write
from art import text2art
import time
print(text2art('welcome'))
print(text2art('             to   my  tool            ',font='small'))
# data
top_10ports=[80,443,8080,27017,5432,22,21,3389,3306,53,25,465,587,545,]
with open ("Data.txt","r") as f:
    with open("scan ports results.txt", "w") as file:
     for line in f:
        target=line.strip()
        Write.Print(f"\n[*] Scanning target {target} in top 10 ports\n",Colors.cyan_to_blue,interval=0.02)
        Write.Print('A second...... ',Colors.black_to_white,interval=0.02)
        print("")
        time.sleep(1)  # for Marketing

        file.write(f"********************Scan Results for {target}*********************\n")
        file.write("="*10 + "\n")
        for port in top_10ports:  #loop#
                try:                    
                  service = socket.getservbyport(port) #port service
                except OSError:
                  service = "Unknown"
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #protocole IPv4 and TCP3-way handshake
                s.settimeout(1.0)
                result = s.connect_ex((target, port))
        #condition
                if result == 0:                            
                      output = f"[+] Port {port} is OPEN  | Service: {service}\n"
                      Write.Print(output,Colors.green,interval=0.02)
                      file.write(output + "\n")
                      
                else:
                      Write.Print(f"[-] Port {port} is closed | Service: {service}\n",Colors.red)
                       
                s.close()

Write.Print("\n[+] Scan complete. Open ports saved to 'scan_results.txt'",Colors.dark_gray,interval=0.2)



















































