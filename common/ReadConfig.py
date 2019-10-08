import  configparser
import os

def getBrowserinfo(name):
    cf = configparser.ConfigParser()
    cfpath = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
    cf.read(cfpath)
    browsername = cf.get('browser', name)
    return browsername

# print(getBrowserinfo('BrowserName'))
