__author__ = 'cerias'

import requests
import async

from logger import log

from threading import Thread

class Serverpush:

    def __init__(self,server):

        self._server = server

        pass


    def push(self,endpoint,data):
        currentEndpoint = "{}{}".format(self._server,endpoint)
        header = {'Content-Type': 'application/json'}
        req = async.get(currentEndpoint,params=data,header=header)
        # request = urllib2.Request(url=currentEndpoint,data=data,headers={'Content-Type': 'application/json'})
        # response = urllib2.urlopen(request)
        log.debug(req.text)

        return req.text
