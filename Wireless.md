<a href="https://github.com/the-AY/Cyber_Security"> Main</a>
## Wireless Attacks 
### Nmap <br>
-> Nmap is an open-source network scanner that is used to recon/scan networks. It is used to discover hosts, ports, and services along with their versions over a network.
It sends packets to the host and then analyzes the responses in order to produce the desired results. It could even be used for host discovery, operating system detection,
or scanning for open ports. It is one of the most popular reconnaissance tools.
why we use this tool? <br>
The first step to start vulnerability analysis  is know more about the victim's System , so to know the  OS , open ports and many more crucial information.<br>
<a href ="https://nmap.org/"> Nmap Website</a> <br>


### Packet Injection 
Packet injection Using supported Wi-Fi Adapter , Packet Injection is also known as "MITM" Man In The Middle" Attack .<br>

Prerequisite:- Check whether the Wi-Fi adaptor supports Packet injection<br>
 1) $ :-
     ip a 
 -> check all the current  eth and Wi-Fi devices and select the card of  your choice <br>
     sudo ip link set dev (Wi-Fi card name) down
     sudo iwconfig (Wi-Fi card name) mode monitor
 if you get an error the adapter does support monitor mode <br>
     sudo iwconfig (Wi-Fi card name) mode managed
     sudo ip link set dev (Wi-Fi card name) up
### Wireshak
<a href ="https://www.wireshark.org/">Wireshark</a><br>
Wireshark is a tool used for network protocol analyzing 

### Bettercap 
So what is  Bettercap? <br>
-> Bettercap is a HID (Human Iterface Device) hijacker so basically your Mouse ,keyboard etc.. is a HID device
bettercap is a powerful, easily extensible and portable framework written in Go which aims to offer to security researchers, red teamers and reverse engineers an easy to use, all-in-one solution with all the features they might possibly need for performing reconnaissance and attacking WiFi networks, Bluetooth Low Energy devices, wireless HID devices and IPv4/IPv6 networks.


### Aircrack-ng 

used for :-

 Monitoring: Packet capture and export of data to text files for further processing by third party tools <br>
Attacking: Replay attacks, deauthentication, fake access points and others via packet injection <br>
Testing: Checking WiFi cards and driver capabilities (capture and injection) <br>
    Cracking: WEP and WPA PSK (WPA 1 and 2) <br>

