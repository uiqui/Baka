import os;

os.system("rm /root/Output-01.csv");

#os.system("iw phy phy0 interface add mon0 type monitor");
#os.system("ifconfig mon0 up");

os.system("airodump-ng -w Output --output-format csv wlan0");
