import os;
    
#os.system("rm /root/Output-01.csv");

#b8:27:eb:5c:d6:00//inbuild
#50:3e:aa:5d:45:5e//tl
text = os.popen("iw dev | grep 'phy\|wlan\|addr'").read();
text = text.split('\n');
i = len(text)-1;

while i!=-1:
    if text[i].find("b8:27:eb:5c:d6:00") != -1:
        while True:
            i=i-1;
            if text[i][0:3] == 'phy':
                phy= 'phy' + text[i][4];                
                break;
        break;    
    i=i-1;
    
os.system("iw phy "+ phy +" interface add mon0 type monitor");
os.system("ifconfig mon0 up");
os.system("airodump-ng -w Output --output-format csv mon0");

#os.system("airodump-ng -w Output --output-format csv " + wlan);
