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
    curInstanceOfData = []; #current
    hisInstanceOfData = []; #old
    flag = False;
    with open("/root/myOutput-01.csv","r") as f:
        for line in f:
            if line is not "\n":   #ignore empty lines             
                cells = line.split(",");
                i=0;
                length = len(cells);
                while i < length:#go trough sliced line and remove white spaces
                    cells[i] = cells[i].strip();
                    i=i+1;
                if cells[0].startswith("Station MAC"):#if old table switch container
                    flag = True;
                if flag:#check what table should put info
                    hisInstanceOfData.append(cells);
                else:
                    curInstanceOfData.append(cells);
    #printArr(curInstanceOfData);
    #printArr(hisInstanceOfData);

    f.close();
    #remove for infinite loop
    #time.sleep(60);
    break;
