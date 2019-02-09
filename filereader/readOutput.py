import time;

def printArr(instance):
    for cell in instance:
        for celll in cell:
            print(celll + "/");
        print("\n");
    print("///////////////////////////////////////");
    return;

#beginingOfTable = "Station MAC".strip();

while True:
    wifiInstanceOfData = []; #wifi
    clientInstanceOfData = []; #client
    with open("/root/myOutput-01.csv","r") as f:
        for line in f:
            if line is not "\n":   #ignore empty lines             
                cells = line.split(",");                
                i=0;
                length = len(cells);
                #print(length);
                
                while i < length:#go trough sliced line and remove white spaces
                    cells[i] = cells[i].strip();
                    i=i+1;
                    
                if length == 15:#check what table should put info
                    wifiInstanceOfData.append(cells);
                else:
                    clientInstanceOfData.append(cells);
                    
    #printArr(wifiInstanceOfData);
    #printArr(oldInstanceOfData);

    f.close();
    #remove for infinite loop
    #time.sleep(60);
    break;
