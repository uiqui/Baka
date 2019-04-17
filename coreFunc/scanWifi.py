import time;
import datetime;
import os;
import math;
import json;
import urllib.request;
from threading import Thread;

def printArr(instance):
    for cell in instance:
        for celll in cell:
            print(str(celll) + "/");
        print("**************");
    print("///////////////////////////////////////");
    return;

def waitForTL():
    i=0;
    while i!=2:
        text = os.popen("ifconfig | grep 'wlan'").read();
        arrText = text.split("\n");
        i=0;
        for line in arrText:
            outFind = line.find('UP');
            if outFind !=-1:
               i=i+1;
        time.sleep(2);
def findWifiInterface(arrText):
    i = len(arrText)-1;

    while i!=-1:
        if arrText[i].find("wlan") != -1:
            if arrText[i+1].find("50:3e:aa:5d:45:5e") == -1:
                while True:
                    if arrText[i][0:3] == 'phy':
                        phy= 'phy' + arrText[i][4];                
                        return phy;
                    i=i-1;
        i=i-1;
def wifiMon():
    text = os.popen("iw dev | grep 'phy\|wlan\|addr'").read();
    arrText = text.split('\n');
    phy = findWifiInterface(arrText);
    os.system("iw phy "+ phy +" interface add mon0 type monitor");
    os.system("ifconfig mon0 up");

#fspl algorithm (km)
# fspl - intensity of signal
# f - frequency from the signal
def calculateDistance(f,fspl):
    f = float(f);
    f = f / 1000;
    f = math.log10(f);
    fspl = float(fspl);
    fspl = abs(fspl);
    f = 20 * f;
    c = float(92.45);
    exp = float(float(fspl) - f - c)/20;
    exp = exp + 3;    #km --> m
    d = float(math.pow(10,exp));
    return d;
def systemGetScan():
    text = os.popen("iw wlan1 scan | grep '(on wlan1)\|freq: \|signal: \|SSID: '").read();
    return text;
       
def getUploadData():
    wifiInstanceOfData = []; #wifi

    text =systemGetScan();
    arrText = text.split('\n');
    for line in arrText:
        if line != '\n':
            lineS = line.strip();

            find = lineS.find('on wlan1');
            if find !=-1:
                lineCell = [];
                #mac
                lineCell.append(lineS[4:21]);
            find = lineS.find('freq');
            if find !=-1:
                #freq
                lineCell.append(lineS[6:]);
            find = lineS.find('signal');
            if find !=-1:
                #pwr
                lineCell.append(lineS[9:-4]);
            find = lineS.find('SSID');
            if find !=-1:
                #ssid
                lineCell.append(lineS[6:]);
                lineCell.append(calculateDistance(lineCell[1],lineCell[2]));
                lineCell.pop(1);
                wifiInstanceOfData.append(lineCell);
                
    try:
        postRequest(wifiInstanceOfData);
    except:
       return;
    
def postRequest(instance):
    instance.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"));
    cell =[];
    cell.append(instance);
    params = json.dumps(cell).encode('utf8');
    url = 'http://iolab.sk:8033/~venczel/jsonPost.php';
    req = urllib.request.Request(url,data=params,headers={'content-type': 'application/json'});
    response = urllib.request.urlopen(req);    
    parseResponse(response.read().decode('utf8'));
    
def parseResponse(response):
    find = response.find('0');
    if find !=-1:
        return;
    find = response.find('1');
    if find !=-1:
        os.system("rm /root/Output-01.csv");
        os.system("sudo halt");
    find = response.find('2');
    if find !=-1:
        os.system("rm /root/Output-01.csv");
        os.system("sudo reboot");
#main
waitForTL();
#wifiMon();
while True:
    getUploadData();
