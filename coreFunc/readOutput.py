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
        print("");
    print("///////////////////////////////////////");
    return;

def waitForTL():
    i=0;
    while i!=2:
        text = os.popen("ifconfig | grep 'wlan'").read();
        arrText = text.split("\n");
        i=0;
        for line in arrText:
            outFind = line.find('RUNNING');
            if outFind !=-1:
               i=i+1;
        time.sleep(2);
        
def wifiMon():
    os.system("python /root/Documents/project/startup/airdump.py");
    
def getChannel():
    result =[];

    text = os.popen('sudo iwlist wlan0  channel').read();
    splitLine = text.split("\n");
    splitLine.pop(0);
    splitLine.pop(len(splitLine)-1);
    splitLine.pop(len(splitLine)-1);

    for line in splitLine:
        line = line.strip();
        line = line[8:(len(line)-3)];
        splitWords = line.split(" : ");
        if splitWords[0][0] is '0':
            splitWords[0] = splitWords[0][1:];
        result.append(splitWords);

    return result;

#fspl algorithm (km)
# fspl - intensity of signal
# f - frequency from the signal
def calculateDistance(f,fspl):
    f = float(f);
    f = math.log10(f);
    fspl = float(fspl);
    fspl = abs(fspl);
    f = 20 * f;
    c = float(92.45);
    exp = float(float(fspl) - f - c)/20;
    exp = exp + 3;    #km --> m
    d = float(math.pow(10,exp));
    return d;

def fetchData():
    wifiInstanceOfData = []; #wifi
    channelFreq = getChannel();
    try:
        #with open("Output-01.csv","r") as f:
        with open("/root/Output-01.csv","r") as f:
            for line in f:
                if line is not "\n":   #ignore empty lines
                    cells = line.split(",");

                    i = len(cells) - 1;#length
                    length = i;
                    while i >= 0:#go trough sliced line and remove white spaces

                        if i == 0 or  i == 8 or i==13: #0 mac #7 channel #8 pwr #13 essid
                            cells[i] = cells[i].strip();
                        elif i == 3:
                            tmp = cells[i].strip();
                            for ch in channelFreq:
                                if ch[0] == tmp:
                                    cells[i] = ch[1];
                                    break;
                        else:
                            cells.pop(i);
                        i=i-1;

                    if length == 14:#check what table should put info
                        wifiInstanceOfData.append(cells);
    except OSError:
        return;

    f.close();
    if not wifiInstanceOfData:
        return;
    wifiInstanceOfData.pop(0);

    i = len(wifiInstanceOfData)-1;
    while i!= -1:
        if wifiInstanceOfData[i][1].strip() == '-1' or wifiInstanceOfData[i][2].strip() == '-1':
            del wifiInstanceOfData[i]         
        else:
            dist = calculateDistance(wifiInstanceOfData[i][1],wifiInstanceOfData[i][2]);
            wifiInstanceOfData[i].pop(1);
            wifiInstanceOfData[i].append(dist);
        i = i - 1;

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

waitForTL();

t = Thread(target=wifiMon);
t.start();

while True:
    fetchData();
    time.sleep(10);
