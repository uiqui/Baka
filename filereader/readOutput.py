import time;

while True:
    instanceOfData = [];
    with open("/root/wifiData-01.csv","r") as f:
        for line in f:
            if line is not "\n":
                instanceOfData.append(line);
  
    f.close();
    #print(instanceOfData);
    for cell in instanceOfData:
        print(cell + "\n");
    break;
