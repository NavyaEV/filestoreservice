from CommonUtils import CommonUtils
import os

class TestSetup(CommonUtils):
    def run(self):
        baseDir = '%s/..'%os.getcwd()
        status, stdout, stderr = self.execCommandLocal('ls %s'%baseDir)
        print('stdout:\n------\n%s\nstderr:\n------\n%s\n'%(stdout, stderr))
        if status != 0:
            print('Failed to get list of files from project directory')
            return False

        cmd = 'cd %s;echo \'y\'| docker-compose up -d'%baseDir
        status, stdout, stderr = self.execCommandLocal(cmd)
        print('stdout:\n------\n%s\nstderr:\n------\n%s\n'%(stdout, stderr))
        if status != 0:
            print('Failed to start container')
            return False

        cmd = 'cd %s; mkdir sample; echo \'Hello workd\' > sample/sample.txt; tar czf sample.tar sample/'%baseDir
        status, stdout, stderr = self.execCommandLocal(cmd)
        print('stdout:\n------\n%s\nstderr:\n------\n%s\n'%(stdout, stderr))
        if status != 0:
            print('Failed to create tar file')
            return False

        return True

runObj = TestSetup()
runObj.run()
