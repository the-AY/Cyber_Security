V0.1
# <b> Cyber_Security </b>
Cheatlists, Getting Started with Cyber Securityn guide ,Attacks 
## Physical  Access to Victim device 
### USB rubber ducky
 USB rubber Ducky using Ardiuino ATTINY35 or Raspberry pi pico
 <a href ="https://www.google.com/"> Ping Google test </a>
or any other microcontroller which is able to run scripts has has storage for scipts 
the microcontroller device imperonates itself as A HID(Human Interface Device ) device  just like a Keyboard and a Mouse 
and Performs the keystrokes and mouse clicks 
Steps to Start
1) Know which OS the victim is using <br>
2) What kind of attacks you want to do <br>
3) Learn a Appropriate scripting Langauge and write the code

## Remote Access to victim device

## Wireless Attacks 
### Packet Injection 
Packet injection Using supported Wi-Fi Adapter ,Packet Injection is also known as "MITM" Man In The Middle" Attack
Check whether the Wi-Fi adaptor supports Packet injection
 LINUX 
 1) ip a
 -> check all the curret eth and Wi-Fi devices and select the card of  your choice
 2) sudo ip link set dev (Wi-Fi card name) down
 3) sudo iwconfig (Wi-Fi card name) mode monitor
 if you get an error the adapter does support monitor mode
 4) sudo iwconfig (Wi-Fi card name) mode managed
    sudo ip link set dev (Wi-Fi card name) up