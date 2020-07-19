import os

def main():

    testList = ['TestListWhenEmpty.py',
                'TestFileUpload.py',
                'TestFileUploadAgain.py',
                'TestDownload.py'
                ]
    resultsDict = {}
    for test in testList:
        resultsDict[test] = False
    try:
        print('===========Executing Setup===========')
        setupStatus = os.system('python TestSetup.py')
        print(setupStatus)

        for test in testList:
            print('==========Running test %s=========='%test)
            if not os.system('python %s'%test):
                print('%s test failed with error'%test)
            else:
                resultsDict[test] = True
                print('%s test passed successfully'%test)
    finally:
        print('===========ExecutingTeardown===========')
        teardownStatus = os.system('python TestTeardown.py')
        print(teardownStatus)

        print('=========== Test Summary ===========')
        print('Testcase\t\t\tStatus\nTestSetup.py\t\t\t%s\n'%setupStatus)
        for key in resultsDict:
            print('%s\t\t\t%s\n'%(key, resultsDict[key]))
        print('TestTeardown.py\t\t\t%s'%teardownStatus)

if __name__ == '__main__':
    main()
