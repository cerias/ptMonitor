__author__ = 'cerias'
import logging
from ConfigManagement import ConfigMonitor

c = ConfigMonitor()
logging.basicConfig(format=c.getVar('logging','console'), level=logging.DEBUG)
log = logging.getLogger('')

