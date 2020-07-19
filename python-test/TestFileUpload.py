from CommonUtils import CommonUtils
import os

class TestFileUpload(CommonUtils):

    def run(self):

        cmd = 'curl -i -X POST %s -F \'file=@%s/sample.tar\''%(self.uploadUrl, self.baseDir)
        status, stdout, stderr = self.execCommandLocal(cmd)
        print('stdout:\n------\n%s\nstderr:\n------\n%s\n'%(stdout, stderr))
        if status != 0:
            print('Failed to run upload command')
            return False

        if (self.errorCodes["SuccessfulUpload"]["code"] not in stdout or
            self.errorCodes["SuccessfulUpload"]["message"] not in stdout):
            print('Expected error code not found')
            return False

        filesList, stdout = self.getFilesList()
        if 'sample.tar' not in filesList:
            print('Failed to check the file in the files list')
            return False
        print('sample.tar found in file list')
        return True
        

runObj = TestFileUpload()
runObj.run()

