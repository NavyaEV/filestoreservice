import subprocess
from optparse import OptionParser
import json
import os
baseDir = os.getcwd()
errorCodesFile = '%s/ErrorCodes.json'%baseDir
f = open(errorCodesFile, "r")
errorCodes = json.loads(f.read())

class CommonUtils():

    def __init__(self):
        self.uploadUrl = 'http://127.0.0.1:5110/v1/files/'
        self.downloadUrl = 'http://127.0.0.1:5110/v1/files/download'
	self.baseDir = os.getcwd()        
        errorCodesFile = '%s/ErrorCodes.json'%self.baseDir
        f = open(errorCodesFile, "r")
        self.errorCodes = json.loads(f.read())

    def execCommandLocal(self, cmd):
        """
        Summary: Execute given command local
        """
        print('Running command: %s' % cmd)
        proc = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
        stdout, stderr = proc.communicate()
        status = proc.poll()
        return status, stdout, stderr

    def getFilesList(self):

        cmd = 'curl -i -X GET %s'%self.uploadUrl
        status, stdout, stderr = self.execCommandLocal(cmd)
        print('stdout:\n------\n%s\nstderr:\n------\n%s\n'%(stdout, stderr))
        if status != 0:
            print('Failed to run list command')
            return False, stdout
        if (errorCodes["SuccessfulList"]['code'] not in stdout or
            errorCodes["SuccessfulList"]['message'] not in stdout):
            print('Expected error code not found in stdout')
            return False, stdout
        filesList = stdout.split('\n')[-1]
        return filesList, stdout
