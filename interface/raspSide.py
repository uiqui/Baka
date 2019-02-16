#import
import threading;
import os;

from flask import Flask;
from flask import request;
from flask_restful import Resource, Api;

def halt():
    os.system("sudo halt");
def reboot():
    os.system("sudo reboot");
def echo(string):
    os.system("echo " +'"'+ string + '"');

#code part
app= Flask(__name__);

@app.route('/', methods=['GET'])
@app.route('/data', methods=['GET'])
def data():   
    return "<html><body><h1>Executed 0</h1></body></html>";

@app.route('/halt', methods=['POST','GET'])
def halt():   
    return "<html><body><h1>Executed 1</h1></body></html>";

@app.route('/reboot', methods=['POST','GET'])
def reboot():   
    return "<html><body><h1>Executed 2</h1></body></html>";

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=6976,debug=True);#,threaded=True);
