import os;

os.system("rm /root/Output-01.csv");
#settup monitor
os.system("iw phy phy0 interface add mon0 type monitor");
os.system("ifconfig mon0 up");
#call airdump-ng to collect data from surroundings
#os.system("airodump-ng -w wifiData.csv mon0");
os.system("airodump-ng -w Output --output-format csv mon0");
