__author__ = 'cerias'

import sys
from systemInformations import BasicInformations
from webserver import WebServer

info = BasicInformations()
print(info)

s = WebServer('localhost',8090)
s._start()

