import time;

def printArr(instance):
    for cell in instance:
        for celll in cell:
            print(celll + "/");
        print("\n");
    print("///////////////////////////////////////");
    return;
def fetchData():
    wifiInstanceOfData = []; #wifi
    #clientInstanceOfData = []; #client
    with open("/root/Output-01.csv","r") as f:
        for line in f:
            if line is not "\n":   #ignore empty lines             
                cells = line.split(",");                
                
                i = len(cells) - 1;#length
                length = i;
                while i >= 0:#go trough sliced line and remove white spaces

                    if i == 0 or i == 1 :#or i==13: #13 for essid
                        cells[i] = cells[i].strip();
                    else:
                        cells.pop(i);
                    i=i-1;

                if length == 14:#check what table should put info
                    wifiInstanceOfData.append(cells);
                #else:
                    #clientInstanceOfData.append(cells);
                    
    #printArr(wifiInstanceOfData);
    #printArr(clientInstanceOfData);

    f.close();
    wifiInstanceOfData.pop(0);
    return wifiInstanceOfData;
#MAIN thread

#while True:
    #printArr(fetchData());    
    #remove for infinite loop
    #time.sleep(60);
#    break;
