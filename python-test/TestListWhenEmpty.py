from CommonUtils import CommonUtils
import os
import json

class TestListWhenEmpty(CommonUtils):

    def run(self):
        list, out = self.getFilesList()
        list = json.loads(list)
        if list == []:
            print('No files found in store as expected')
            return True
        else:
            print('Files are detected in store')
            return False

runObj = TestListWhenEmpty()
runObj.run()

