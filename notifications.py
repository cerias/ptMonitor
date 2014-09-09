__author__ = 'cerias'

import urllib2


from logger import log

from threading import Thread

class Serverpush:

    def __init__(self,server):

        self._server = server

        pass


    def push(self,endpoint,data):
        currentEndpoint = "{}{}".format(self._server,endpoint)
        header = {'Content-Type': 'application/json'}
        request = urllib2.Request(url=currentEndpoint,data=data,headers={'Content-Type': 'application/json'})

        response = urllib2.urlopen(request)
        dat = response.read()
        response.close()
        log.debug(dat)

        return dat

