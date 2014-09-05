__author__ = 'cerias'

from systemInformations import BasicInformations
from webserver import WebServer
from ConfigManagement import ConfigMonitor
from logger import log
from notifications import Serverpush
import json

class Main():

    def __init__(self):
        # init config reader
        self._config = ConfigMonitor()
        # start debugger
        log.debug(self._config.getVar('logging','dir'))

        # init serverpush
        self._push = Serverpush(self._config.getVar('cluster','host'))

        # basic informations
        info = BasicInformations()

        # register on server
        if self._config.getVar('cluster','id')!='':
            print(self._config.getVar('cluster','id'))
        else:
            log.info("reciving new id")
            response = self._push.push('register',json.dumps(info.getInfo()))

            print(response)


        # start webserver
        s = WebServer(self._config.getVar("webserver","host"),self._config.getVar("webserver","port"))
        s.start()
        pass

    def test(self):
        pass

m = Main()


