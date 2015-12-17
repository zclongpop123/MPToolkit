#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Wed, 16 Dec 2015, 10:39:28
#========================================
import re, pymel.core
import maya.cmds as mc
import maya.OpenMaya as OpenMaya
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def getGeometrys():
    '''
    List all of poly and nurbsSurface geometrys...
    '''
    geometrys = mc.listRelatives(mc.ls(type=('mesh', 'nurbsSurface')) or ['persp'], p=True, path=True) or list()
    return geometrys



def checkingDuplicatesNames():
    '''
    List all of dupliacates name...
    '''
    mSelectionList = OpenMaya.MSelectionList()
    data = ' '.join(mc.ls())
    for obj in re.findall('\S+\|\S+', data):
        if not re.search('\|', obj):
            continue
        mSelectionList.add(obj)
    return mSelectionList



def checkingDefaultName():
    '''
    List all of geometrys used default name...
    '''
    mSelectionList = OpenMaya.MSelectionList()

    geometrys = ' '.join(getGeometrys())
    Results = dict.fromkeys([x[0] for x in re.findall('(((?<=\s)|^)[a-zA-Z0-9]+((?=\s)|$))', geometrys)]).keys()
    for geo in Results:
        mSelectionList.add(geo)

    return mSelectionList



def checkingDuplacatesShape():
    '''
    List all of geometrys with multy shapes
    '''
    mSelectionList = OpenMaya.MSelectionList()
    for obj in getGeometrys():
        if len(mc.listRelatives(obj, s=True, path=True) or []) < 2:
            continue
        mSelectionList.add(obj)
    return mSelectionList   




def checkingCenterPoints():
    '''
    '''    
    mSelectionList = OpenMaya.MSelectionList()
    for geo in getGeometrys():
        transform = OpenMaya.MFnTransform(pymel.core.PyNode(geo).__apiobject__())
        value = 0
        rotateP = transform.rotatePivot(OpenMaya.MSpace.kWorld)
        scaleP  = transform.scalePivot(OpenMaya.MSpace.kWorld)
        for a in 'xyz':
            value += getattr(rotateP, a)
            value += getattr(scaleP,  a)

        if round(value, 4) == 0:
            continue

        mSelectionList.add(geo)

    return mSelectionList




def checkingHiearachy():
    '''
    List all of geometry objects in top leavel...
    '''
    mSelectionList = OpenMaya.MSelectionList()

    for geo in mc.ls(assemblies=True):
        if not mc.listRelatives(geo, s=True, typ=('mesh', 'nurbsSurface')):
            continue
        mSelectionList.add(geo)

    return mSelectionList




def checkingAttributes():
    '''
    List all of geometrys without freeze...
    '''
    mSelectionList = OpenMaya.MSelectionList()

    for geo in getGeometrys():
        res = True
        res = res and sum(mc.getAttr('{0}.t'.format(geo))[0]) == 0
        res = res and sum(mc.getAttr('{0}.r'.format(geo))[0]) == 0
        res = res and sum(mc.getAttr('{0}.s'.format(geo))[0]) == 3

        if not res:
            mSelectionList.add(geo)

    return mSelectionList



def checkingVertex():
    '''
    List all of geometrys with vertex is not zero...
    '''
    mSelectionList = OpenMaya.MSelectionList()

    geometrys = getGeometrys()
    pointType = {'nurbsSurface':'cv', 'mesh':'vtx'}

    for geo in geometrys:
        shpType = mc.nodeType(mc.listRelatives(geo, s=True, path=True)[0])
        vertexValues = openMultiarray(mc.getAttr('%s.%s[:]'%(geo, pointType[shpType])))

        if round(sum(vertexValues), 4) == 0:
            continue

        mSelectionList.add(geo)

    return mSelectionList




def checkingHistory():
    '''
    List all of geometrys have history...
    '''
    mSelectionList = OpenMaya.MSelectionList()

    for geo in getGeometrys():
        if not mc.listHistory(geo, pdo=True):
            continue
        mSelectionList.add(geo)

    return mSelectionList



def openMultiarray(Array):
    '''
    [1, [2, [3, 4], 5], 6] -> [1, 2, 3, 4, 5, 6]
    (1, (2, (3, 4), 5), 6) -> (1, 2, 3, 4, 5, 6)
    '''
    for Item in Array:
        if isinstance(Item, (tuple, list)):
            for i in openMultiarray(Item):
                yield i
        else:
            yield Item
