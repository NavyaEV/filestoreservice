from CommonUtils import CommonUtils
import os

class TestTeardown(CommonUtils):
    def run(self):

        contianerId = self.getContainerID()
        if not contianerId:
            return False

        cmd = 'docker kill %s'%contianerId
        status, stdout, stderr = self.execCommandLocal(cmd)
        print('stdout:\n------\n%s\nstderr:\n------\n%s\n'%(stdout, stderr))
        if status != 0:
            print('Failed to start container')
            return False

        contianerId = self.getContainerID()
        if contianerId != False or contianerId != '':
            print('Container still in running status! Try to kill manuall')

        cmd = 'rm -rf sample* Header.txt'
        status, stdout, stderr = self.execCommandLocal(cmd)
        return True

    def getContainerID(self):
        cmd = 'docker ps| grep filestoreservice | awk \'{print $1}\''
        status, stdout, stderr = self.execCommandLocal(cmd)
        print('stdout:\n------\n%s\nstderr:\n------\n%s\n'%(stdout, stderr))
        if status != 0:
            print('Failed to get list of files from project directory')
            return False
        return stdout[:-1]

runObj = TestTeardown()
runObj.run()
