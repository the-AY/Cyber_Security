reference :-
 <a href ="https://www.geeksforgeeks.org/top-10-kali-linux-tools-for-hacking/"> Geeks for Geeks </a>
  <a href ="https://www.google.com/"> Ping Google test </a>

Nmap
Nmap is an open-source network scanner that is used to recon/scan networks. It is used to discover hosts, ports, and services along with their versions over a network.
It sends packets to the host and then analyzes the responses in order to produce the desired results. It could even be used for host discovery, operating system detection,
or scanning for open ports. It is one of the most popular reconnaissance tools.
2. Burp Suite

Burp Suite is one of the most popular web application security testing software. It is used as a proxy, so all the requests from the browser with the proxy pass through it. 
And as the request passes through the burp suite,
 it allows us to make changes to those requests as per our need which is good for testing vulnerabilities like XSS or SQLi or even any vulnerability related to the web.
Kali Linux comes with burp suite community edition which is free but there is a paid edition of this tool known as burp suite professional which has a lot many functions as compared to burp suite community edition.
3. Wireshark

Wireshark is a network security tool used to analyze or work with data sent over a network. It is used to analyze the packets transmitted over a network. These packets may have information like the source IP and the destination IP, the protocol used, the data, and some headers. The packets generally have an extension of “.pcap” which could be read using the Wireshark tool.

4. metasploit Framework

Metasploit is an open-source tool that was designed by Rapid7 technologies. It is one of the world’s most used penetration testing frameworks. It comes packed with a lot of exploits to exploit the vulnerabilities over a network or operating systems. Metasploit generally works over a local network but we can use Metasploit for hosts over the internet using “port forwarding“. Basically Metasploit is a CLI based tool but it even has a GUI package called “armitage” which makes the use of Metasploit more convenient and feasible.
5. aircrack-ng

Aircrack is an all in one packet sniffer, WEP and WPA/WPA2 cracker, analyzing tool and a hash capturing tool. It is a tool used for wifi hacking. It helps in capturing the package and reading the hashes out of them and even cracking those hashes by various attacks like dictionary attacks. It supports almost all the latest wireless interfaces.
6. Netcat

Netcat is a networking tool used to work with ports and performing actions like port scanning, port listening, or port redirection. This command is even used for Network Debugging or even network daemon testing. This tool is considered as the Swiss army knife of networking tools. It could even be used to do the operating related to TCP, UDP, or UNIX-domain sockets or to open remote connections and much more.
7. John the Ripper

John the Ripper is a great tool for cracking passwords using some famous brute for attacks like dictionary attack or custom wordlist attack etc. It is even used to crack the hashes or passwords for the zipped or compressed files and even locked files as well. It has many available options to crack hashes or passwords.

8. sqlmap

sqlmap is one of the best tools to perform SQL injection attacks. It just automates the process of testing a parameter for SQL injection and even automates the process of exploitation of the vulnerable parameter. It is a great tool as it detects the database on its own so we just have to provide a URL to check whether the parameter in the URL is vulnerable or not, we could even use the requested file to check for POST parameters.
9. Autopsy(forensics)

Autopsy is a digital forensics tool that is used to gather the information form forensics. Or in other words, this tool is used to investigate files or logs to learn about what exactly was done with the system. It could even be used as a recovery software to recover files from a memory card or a pen drive.
10. Social Engineering Toolkit

Social Engineering Toolkit is a collection of tools that could be used to perform social engineering attacks. These tools use and manipulate human behavior for information gathering. it is a great tool to phish the websites even.

1. Disk Forensics : autopsy (Free)
- Encase
- FTK
- Magnet Axiom

2. Mobile Forensics 
- oxygen forensic
- UFED Forensic

sshgit (this tools is used to search openly available in github)

what is rootkit 
how to make rootkits
how to prevent rootkit attacks