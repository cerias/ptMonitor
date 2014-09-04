__author__ = 'cerias'

import platform

class BasicInformations:

    def __init__(self):
        pass

    def getInfo(self):
        data = [{
            'system': platform.system(),
            'type': platform.machine(),
            'hostname': platform.node()
        }]

        return data
