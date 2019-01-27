import os;
import subprocess;
import time;
#settup monitor
def initMon():
  os.system("iw phy phy0 interface add mon0 type monitor");
  os.system("ifconfig mon0 up");

#initMon();

os.system("airodump-ng -w myOutput --output-format txt mon0");

