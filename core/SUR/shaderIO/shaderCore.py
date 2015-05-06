#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 28 Apr 2015 09:30:48
#========================================
import os.path
import maya.cmds as mc
from mpUtils import ioTool
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

def getShaders():
    '''
    get SG nodes by select geometrys...
    '''
    shaders = list()

    objects = mc.ls(sl=True)
    for obj in objects:
        shape = mc.listRelatives(obj, s=True, path=True)
        if not shape:
            continue
        material_SG = mc.listConnections(shape[0], type='shadingEngine')
        shaders.extend(material_SG)

    shaders = [m for i, m in enumerate(shaders) if m not in shaders[:i]]
    return shaders




def getObjectsByShader(shaders=list()):
    '''
    get geometrys or geometry faces by shader node...
    '''
    object_data = dict()

    for shd in shaders:
        if shd == 'initialShadingGroup':
            continue

        input_shd = mc.listHistory(shd, pdo=1)[1]
        mc.hyperShade(objects=input_shd)
        object_data[shd] = mc.ls(sl=True, fl=True)

    return object_data




def setShadertoObject(shader_data = dict()):
    '''
    connect shaders to geometrys...
    '''
    for shd, obj in shader_data.iteritems():
        target = obj

        if isinstance(obj, basestring):
            if not mc.objExists(obj):continue

        elif isinstance(obj, list):
            target = [f for f in obj if mc.objExists(f)]
        if not target:continue

        mc.sets(target, e=True, forceElement=shd)





def exportShader(filePath, shaders=list()):
    '''
    export shaders to ma file...
    '''
    if not shaders:return 

    mc.select(shaders, ne=True)
    mc.file(filePath, es=True, pr=True, typ='mayaAscii')




def importShader(filePath):
    '''
    import shaders from ma file...
    '''
    if not filePath:return
    mc.file(filePath, i=True)




def exportGeometryShader():
    '''
    export shaders and connected data...
    '''
    path = mc.fileDialog2(fm=0, ff='Maya ASCII (*.ma);;')
    if not path:return

    shader_file_path = path[0]
    shader_data_path = '%s.json'%os.path.splitext(path[0])[0]

    shaders = getShaders()
    data    = getObjectsByShader(shaders)

    exportShader(shader_file_path,     shaders)
    ioTool.writeData(shader_data_path, data)



def importGeometryShader():
    '''
    import shaders and apply to target geometrys...
    '''
    path = mc.fileDialog2(fm=1, ff='Maya ASCII (*.ma);;')
    if not path:return

    shader_file_path = path[0]
    shader_data_path = '%s.json'%os.path.splitext(path[0])[0]

    importShader(shader_file_path)
    shader_data = ioTool.readData(shader_data_path)

    setShadertoObject(shader_data)