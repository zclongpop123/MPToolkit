#=============================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Wed, 25 Jun 2014 14:43:02
#=============================================
import sys, re, os, string
import maya.cmds as mc

#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
POSITION_INDEX = 0
DESCRIPTION_INDEX = 1
NODETYPE_INDEX = 2
INDEX_INDEX = 3


def compileWindowsFileName(fullPath):
    '''
    build a not exists windows file name...
    Exp:  
        D:/text         -> D:/text(1)         -> D:/text(2)         -> D:/text(3) ... D:/text(n+1)
        E:/Document.txt -> E:/Document(1).txt -> E:/Document(2).txt -> E:/Document(3).txt ... E:/Document(n+1).txt
    '''
    if not os.path.isfile(fullPath) and not os.path.isdir(fullPath):
        return fullPath
    
    fname, fextension = os.path.splitext(fullPath)
    res = re.search('\(\d+\)$', fname)
    if res:
        index = string.zfill(int(res.group()[1:-1]) + 1, len(res.group()) - 2)
        fname  = re.sub('\(\d+\)$', '(%s)'%index, fname)
    else:
        fname      = '%s(1)'%fname
    fullName = fname + fextension
    
    return compileWindowsFileName(fullName)





def compileMayaObjectName(objectName):
    '''
    build a not exists maya object name...
    Exp: 
        pCube  -> pCube1  -> pCube2  -> pCube3  -> pCube4 ...  pCuben+1
        pSphere -> pSphere1 -> pSphere2 -> pSphere3 -> pSphere4 ... pSpheren+1
    '''
    if not mc.objExists(objectName):
        return objectName
    
    res = re.search('\d+$', objectName)
    if res:
        index = string.zfill(int(res.group()) + 1, len(res.group()))
        result   = re.sub('\d+$', index, objectName)    
    else:
        result   = '%s1'%(objectName)
    
    return compileMayaObjectName(result)





def SerializationObjectNames(objectList, nameFormat='Temp*', start=0, padding=3):
    '''
    objectList must is a list or a tuple
    nameFormat mutst have one " * "
    Exp:
            [pCulbe,  pCulbe1, pCulbe2, pCulbe3, pCulbe4] -> temp*
        ->  [temp000, temp001, temp002, temp003, temp004] 
    
            [pCulbe,  pCulbe1, pCulbe2, pCulbe3, pCulbe4] -> C_temp*_geo_0
        ->  [C_temp000_geo_0, C_temp001_geo_0, C_temp002_geo_0, C_temp003_geo_0, C_temp004_geo_0] 
    '''
    if not isinstance(objectList, (list, tuple)):
        return
    
    if nameFormat.count('*') != 1:
        return
    
    newNameList = []
    for i, obj in enumerate(objectList):
        newName = compileMayaObjectName(nameFormat.replace('*', string.zfill(i + start, padding)))
        newNameList.append(newName)
    return newNameList




def SerializationFileNames(path, nameFormat='Temp*', start=0, padding=3):
    if not os.path.isdir(path):
        return
    
    if nameFormat.count('*') != 1:
        return
    
    #- get files -
    files = os.listdir(path)
    
    for i, f in enumerate(files):
        #- build name
        fextension = os.path.splitext(f)[-1]
        NewName = nameFormat.replace('*', string.zfill(i + start, padding)) + fextension
        #- rename
        os.rename(os.path.join(path, f), compileWindowsFileName(os.path.join(path, NewName)))





# Get Name String Parts.
def getPosition(nameString):
    if not checkValidNameString(nameString):
        return None

    return nameString.split('_')[POSITION_INDEX]




def getDescription(nameString):
    if not checkValidNameString(nameString):
        return None

    return nameString.split('_')[DESCRIPTION_INDEX]




def getNodeType(nameString):
    if not checkValidNameString(nameString):
        return None

    return nameString.split('_')[NODETYPE_INDEX]




def getIndex(nameString, asInt=False):
    if not checkValidNameString(nameString):
        return None

    index = nameString.split('_')[INDEX_INDEX]
    if not asInt:
        return index
    else:
        return int(index)


# Substitute string parts.
def subPosition(nameString, position):
    if not checkValidNameString(nameString):
        return nameString

    valid_prefix = ['C', 'L', 'R']

    if not position[0] in valid_prefix and int(position[1:]):
        sys.stderr.write("String '%s' is not a valid position." % (position))
        return nameString

    return '%s_%s' % (position, nameString.split('_', 1)[-1])





def subDescription(nameString, description):
    if not checkValidNameString(nameString):
        return nameString

    if not isinstance(description, basestring):
        sys.stderr.write("String '%s' is not a valid description." % (description))
        return nameString

    splitName = nameString.split('_')
    return '%s_%s_%s_%s' % (splitName[POSITION_INDEX], description,
        splitName[NODETYPE_INDEX], splitName[INDEX_INDEX])





def addDescription(nameString, description):
    if not checkValidNameString(nameString):
        return nameString

    if not isinstance(description, basestring):
        sys.stderr.write("String '%s' is not a valid description." % (description))
        return nameString

    oldDescription = getDescription(nameString)
    return subDescription(nameString, oldDescription + description[0].upper() + description[1:])




   
def subNodeType(nameString, nodeType):
    if not checkValidNameString(nameString):
        return nameString

    if not isinstance(nodeType, basestring) and len(nodeType) == 3:
        sys.stderr.write("String '%s' is not a valid node type." % (nodeType))
        return nameString

    splitName = nameString.split('_')
    return '%s_%s_%s_%s' % (splitName[POSITION_INDEX], splitName[DESCRIPTION_INDEX],
        nodeType, splitName[INDEX_INDEX])





def subIndex(nameString, index):
    if not checkValidNameString(nameString):
        return nameString

    if not isinstance(index, (int, long)) or int(index):
        sys.stderr.write("Input '%s' is not a valid index." % (str(index)))
        return nameString

    return '%s_%s' % (nameString.rsplit('_', 1)[0], str(index))





#    Name Validity Checks
def checkValidNameString(nameString):
    ''' Checks a string to see if it complies with the node naming convention.'''

    result = True

    splitName = nameString.rsplit(':', 1)[-1].split('_')

    #    Convention Check
    if not len(splitName) == 4:
        result = False
        return result

    #    Position Check
    if not checkValidPosition(position=splitName[0]):
        result = False

    #    Description Check
    if not checkValidDescription(description=splitName[1]):
        result = False

    #    Type Check
    if not checkValidNodeType(nodeType=splitName[2]):
        result = False

    #    Index Check
    if not checkValidIndex(index=splitName[3]):
        result = False

    return result




  
def checkValidPosition(position):
    #    check type
    if not isinstance(position, basestring):
        return False

    #    check length
    if not len(position) > 0:
        return False

    #    check the first letter is valid
    if not position[0] in ['C', 'L', 'R']:
        return False

    #    check the index if applicable
    if len(position) > 1:
        try:
            int(position[1:])
        except:
            return False

    return True





def checkValidNodeType(nodeType):
    #    check type
    if not isinstance(nodeType, basestring):
        return False

    #    check length
    if not len(nodeType) == 3:
        return False

    return True




def checkValidDescription(description):
    #    check type
    if not isinstance(description, basestring):
        return False

    #    check length
    if not len(description) > 0:
        return False

    return True




def checkValidIndex(index):
    #    check type
    try:
        int(index)
    except:
        return False

    return True



# String Conversion
def camelCaseToList(inputString, titleCase=True):
    initList = re.findall('^[a-z]+|[A-Z][a-z]+|[A-Z]|[0-9]+', inputString)
    cleanList = list()

    for i, item in enumerate(initList):

        if not i:
            if titleCase:
                cleanList.append(item.title())
            else:
                cleanList.append(item)

        else:
            if len(item) > 1:
                cleanList.append(item)

            else:
                if cleanList[-1].isupper() and item.isupper():
                    cleanList[-1] += item

                else:
                    cleanList.append(item)

    return cleanList



   
def camelCaseToNiceString(inputString):
    return listToNiceString(camelCaseToList(inputString))




def listToNiceString(inputList):
    result = str()

    for i, token in enumerate(inputList):

        # Keep upper case blocks
        if token.isupper(): result += token

        # Otherwise make them title case.
        else: result += token.title()

        if i < (len(inputList) - 1):
            result += ' '

    return result

 
 

def niceNameToCamelCase(inputString, leadingCapital=False):
    result = str()

    for i, token in enumerate(inputString.split(' ')):
        if not i and leadingCapital:
            result += token
        else:
            result += token.title()

    return result
