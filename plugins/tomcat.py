__author__ = 'cerias'


from logger import log
from subprocess import call
from ConfigManagement import ConfigPlugin

class manager:

    def __init__(self):
        self._c = ConfigPlugin("tomcat")
        self._url = "http://{}:{}@127.0.0.1/manager/text/".format(self._c.getVar("auth","username"),self._c.getVar("auth","password"))
        pass



    def deploy(self):
        url="{}deploy?path={}&update=true&war=file:{}".format(self._url,self._c.getVar("default","warName"),self._c.getVar("default","warName"))
        call(["curl",url])
        pass


    def undeploy(self):
        url="{}undeploy?path={}".format(self._url,self._c.getVar("default","warName"))
        call(["curl",url])
        pass


    def start(self):
        url="{}undeploy?path={}".format(self._url,self._c.getVar("default","warName"))
        pass


    def stop(self):
        url="{}undeploy?path={}".format(self._url,self._c.getVar("default","warName"))
        pass







url="http://console:console@127.0.0.1:8080/manager/text/deploy?path=/test&update=true&war=file:/home/cerias/IdeaProjects/testProjekt/testProjekt/test.war"


#

# response = urllib2.urlopen(url)
# dat = response.read()
# response.close()
# logging.debug(dat)
