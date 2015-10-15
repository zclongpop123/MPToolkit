#=============================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Fri, 04 Jul 2014 14:25:54
#=============================================
import sys, os, json, tempfile
import publishTool
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

def readData(filePath, log=True):
    '''
    import a file path, read data to return..
    '''
    if not os.path.isfile(filePath):
        return dict()

    if log:
        sys.stdout.write('\nReading file : %s'%filePath)

    f = open(filePath, 'r')
    data = json.load(f)
    f.close()
    return data



def writeData(filePath, data, log=True):
    '''
    give a file path and data, write data to file..
    Exp:
       writeData("D:/Temp.json", {"a":0, "b":1})
    '''
    temp = tempfile.mktemp('.json')
    if log:
        sys.stdout.write('\nWriting file : %s'%filePath)

    f = open(temp, 'w')
    json.dump(data, f, indent=4)
    f.close()

    publishTool.publishFile(temp, filePath)