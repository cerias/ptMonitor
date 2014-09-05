__author__ = 'cerias2'

import ConfigParser

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ConfigMonitor(object):
    __metaclass__ = Singleton

    def __init__(self):
        self._config = ConfigParser.RawConfigParser()
        self._config.read('conf/monitor.conf')
        pass

    def getVar(self,section,var):
        return self._config.get(section,var)

    def set(self,section,var,value):
        self._config.set(section, var, value)

    def write(self):
        with open('conf/monitor.conf', 'wb') as configfile:
            self.config.write(configfile)

class ConfigPlugin(object):
    __metaclass__ = Singleton

    def __init__(self,plugin):
        _config = ConfigParser.RawConfigParser()
        _pluginName = "{}{}{}".format("conf",plugin,".conf")
        _config.read(plugin)
        pass

    def getPlugin(self):
        return self._pluginName

    def getVar(self,section,var):
        return self._config.get(section,var)

    def set(self,section,var,value):
        self._config.set(section, var, value)

    def write(self):
        with open('conf/monitor.conf', 'wb') as configfile:
            self.config.write(configfile)