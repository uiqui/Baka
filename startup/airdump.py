import os;
    
#os.system("rm /root/Output-01.csv");

#os.system("iw phy phy0 interface add mon0 type monitor");
#os.system("ifconfig mon0 up");
#b8:27:eb:5c:d6:00//inbuild
#50:3e:aa:5d:45:5e//tl
text = os.popen("ifconfig | grep 'wlan\|ether'").read();
text = text.split('\n');
i = len(text)-1;

while i!=-1:
    if text[i].find("50:3e:aa:5d:45:5e") != -1:
        i=i-1;
        wlan= text[i][0:5];
        break;
    i=i-1;

#os.system("airodump-ng -w Output --output-format csv wlan1");
os.system("airodump-ng -w Output --output-format csv " + wlan);
