__author__ = 'cerias'

import urllib2
import logging
import json
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('conf/monitor.conf')
print(config.get('logging','dir'))

config.set('logging', 'dir', "/home/cerias/")

with open('conf/monitor.conf', 'wb') as configfile:
    config.write(configfile)

config.read('conf/monitor.conf')
print(config.get('logging','dir'))

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
request = urllib2.Request(url='http://localhost:8080/testProjekt/test',data="hallo")
response = urllib2.urlopen(request)
logging.debug(response.read())

class Serverpush:

    def __init__(self,server):

        _server = server

        pass

    def push(self,endpoint,data):
        currentEndpoint = "{}{}".format(self._server,endpoint)
        request = urllib2.Request(url=currentEndpoint,data=data)
        response = urllib2.urlopen(request)
        logging.debug(response.read())
