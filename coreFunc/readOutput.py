import time;
import os;
import math;

def printArr(instance):
    for cell in instance:
        for celll in cell:
            print(str(celll) + "/");
        print("\n");
    print("///////////////////////////////////////");
    return;

def getChannel():
    result =[];

    str = os.popen('sudo iwlist wlan0  channel').read();
    splitLine = str.split("\n");
    splitLine.pop(0);
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
    #print(f);
    #print(fspl);
    f = 20 * f;
    c = float(92.45);
    exp = float(float(fspl) - f - c)/20;
    exp = exp + 3;    #m --> km
    d = float(math.pow(10,exp));
    return d;

def fetchData():
    wifiInstanceOfData = []; #wifi
    channelFreq = getChannel();
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

    f.close();
    wifiInstanceOfData.pop(0);

    i = len(wifiInstanceOfData)-1;
    while i!= 0:
        if wifiInstanceOfData[i][2] != -1:
            dist = calculateDistance(wifiInstanceOfData[i][1],wifiInstanceOfData[i][2]);
            wifiInstanceOfData[i].append(dist);
        else:
            wifiInstanceOfData.pop(i);
        i = i -1;
    
    return wifiInstanceOfData;
print();
printArr(fetchData());
