from CommonUtils import CommonUtils
import os

class TestDownload(CommonUtils):

    def run(self):

        cmd = 'curl -D Header.txt -X GET %s -F \'file=sample.tar\' -o /tmp/sample.tar'%(self.downloadUrl)
        status, stdout, stderr = self.execCommandLocal(cmd)
        print('stdout:\n------\n%s\nstderr:\n------\n%s\n'%(stdout, stderr))
        if status != 0:
            print('Failed to run upload command')
            return False

        cmd = 'cat Header.txt'
        status, stdout, stderr = self.execCommandLocal(cmd)
        print('stdout:\n------\n%s\nstderr:\n------\n%s\n'%(stdout, stderr))
        if (self.errorCodes["SuccessfulDownload"]["code"] not in stdout or
            self.errorCodes["SuccessfulDownload"]["message"] not in stdout):
            print('Expected error code not found')
            return False

        if os.path.exists('/tmp/sample.tar'):
            print('File downloaded successfully')
            return True
        else:
            print('File download failed')
            return False

runObj = TestDownload()
runObj.run()

