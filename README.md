V0.1
# <b> Cyber_Security </b>
Cheatlists, Getting Started with Cyber Security guide ,Attacks .
## Physical  Access to Victim device 
<a href ="https://github.com/the-AY/Cyber_Security/blob/main/Physical.md" > Physical Attacks <a>

## Remote Access to victim device

## Wireless Attacks 

### Packet Injection 
Packet injection Using supported Wi-Fi Adapter , Packet Injection is also known as "MITM" Man In The Middle" Attack .

 ### LINUX 
Prerequisite:- Check whether the Wi-Fi adaptor supports Packet injection
 1) ip a <br>
 -> check all the current  eth and Wi-Fi devices and select the card of  your choice <br>
 2) sudo ip link set dev (Wi-Fi card name) down <br>
 3) sudo iwconfig (Wi-Fi card name) mode monitor <br>
 if you get an error the adapter does support monitor mode <br>
 4) sudo iwconfig (Wi-Fi card name) mode managed <br>
    sudo ip link set dev (Wi-Fi card name) up <br>


  