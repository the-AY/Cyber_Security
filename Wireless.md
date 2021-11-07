## Wireless Attacks 
### Nmap
<a href ="https://nmap.org/"> Nmap Website</a> <br>
-> Nmap is an open-source network scanner that is used to recon/scan networks. It is used to discover hosts, ports, and services along with their versions over a network.
It sends packets to the host and then analyzes the responses in order to produce the desired results. It could even be used for host discovery, operating system detection,
or scanning for open ports. It is one of the most popular reconnaissance tools.



### Packet Injection 
Packet injection Using supported Wi-Fi Adapter , Packet Injection is also known as "MITM" Man In The Middle" Attack .

Prerequisite:- Check whether the Wi-Fi adaptor supports Packet injection
 1) ip a <br>
 -> check all the current  eth and Wi-Fi devices and select the card of  your choice <br>
 2) sudo ip link set dev (Wi-Fi card name) down <br>
 3) sudo iwconfig (Wi-Fi card name) mode monitor <br>
 if you get an error the adapter does support monitor mode <br>
 4) sudo iwconfig (Wi-Fi card name) mode managed <br>
    sudo ip link set dev (Wi-Fi card name) up <br>
