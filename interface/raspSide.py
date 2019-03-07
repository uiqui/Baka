#import of librarys
import json;
import os;

from flask import Flask;
from flask import request;
from flask_restful import Resource, Api;
########################################
#import data reader
import sys;
sys.path.append('/root/Documents/project/coreFunc');
from readOutput import fetchData;
########################################
#basic system functions
def halt():
    os.system("sudo halt");
def reboot():
    os.system("sudo reboot");
def echo(string):
    os.system("echo " +'"'+ string + '"');
########################################
#server side
app= Flask(__name__);

@app.route('/', methods=['GET'])
@app.route('/data', methods=['GET'])
def data():
    #fetchData();
    return "<html><body><h1>"+ json.dumps(fetchData()) +"</h1></body></html>";

@app.route('/halt', methods=['POST','GET'])
def halt_serv():  
    halt(); 
    return '0';

@app.route('/reboot', methods=['POST','GET'])
def reboot_serv():
    reboot();   
    return '0';

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=6976,debug=True);#,threaded=True);
########################################
