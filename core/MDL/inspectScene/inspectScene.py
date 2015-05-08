#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Fri, 24 Oct 2014 10:45:39
#========================================
import string, re, os.path
import maya.cmds as mc
from mpUtils import scriptTool, uiTool
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

ICON_OK       = uiTool.QtGui.QIcon()
ICON_DEFAULT  = uiTool.QtGui.QIcon()
ICON_WARNING  = uiTool.QtGui.QIcon()

IMAGE_OK      = uiTool.QtGui.QPixmap(os.path.join(scriptTool.getScriptPath(), 'icon', 'check.png'))
IMAGE_DEFAULT = uiTool.QtGui.QPixmap(os.path.join(scriptTool.getScriptPath(), 'icon', 'question.png'))
IMAGE_WARNING = uiTool.QtGui.QPixmap(os.path.join(scriptTool.getScriptPath(), 'icon', 'exclamation.png'))

ICON_OK.addPixmap(IMAGE_OK, uiTool.QtGui.QIcon.Disabled, uiTool.QtGui.QIcon.Off)
ICON_DEFAULT.addPixmap(IMAGE_DEFAULT, uiTool.QtGui.QIcon.Disabled, uiTool.QtGui.QIcon.Off)
ICON_WARNING.addPixmap(IMAGE_WARNING, uiTool.QtGui.QIcon.Disabled, uiTool.QtGui.QIcon.Off)

SEARCH_ICON = uiTool.QtGui.QIcon(os.path.join(scriptTool.getScriptPath(), 'icon', 'search.png'))


UIwndClass, baseClass = uiTool.loadUi(os.path.join(scriptTool.getScriptPath(), 'inspectScene.ui'))
class InspectSceneUI(UIwndClass, baseClass):

    def __init__(self, parent=uiTool.getMayaWindow()):
        if uiTool.windowExists('inspectSceneWindow'):
            uiTool.wrapInstance('inspectSceneWindow').__initUI__()
            return

        super(InspectSceneUI, self).__init__(parent)
        self.setupUi(self)
        #-+-+-+-+-+-+-+-+-
        self.btn_InspectScene.setIcon(SEARCH_ICON)
        self.__initUI__()
        #-+-+-+-+-+-+-+-+-
        self.show()
        #-------------

    def __initUI__(self):
        for con in self.groupBox.findChildren(uiTool.QtGui.QSpinBox):
            con.setValue(0)
            con.setStyleSheet('')    

        for con in self.groupBox.findChildren(uiTool.QtGui.QPushButton):
            con.setEnabled(False)
            con.setText('')
            con.setIcon(ICON_DEFAULT)
            con.setStyleSheet('QPushButton{border:none;}')            


    def turnON(self, field, button, value=0):
        field.setValue(value)
        field.setStyleSheet('color: rgb(255, 90, 90)')

        button.setEnabled(True)
        button.setText('Select')
        button.setIcon(ICON_WARNING)
        button.setStyleSheet('')



    def turnOFF(self, field, button, value=0):
        field.setValue(value)
        field.setStyleSheet('')

        button.setEnabled(False)
        button.setText('')
        button.setIcon(ICON_OK)
        button.setStyleSheet('QPushButton{border:none;}')



    def on_btn_InspectScene_clicked(self, args=None):
        if args == None:return
        self.DuplacatesNamesOBJ  = inspectDuplicatesNames()
        self.defaultNameOBJ      = inpectDefaultName()
        self.NoFreeGeometeys     = inspectGeometryAttributes()
        self.pivotErrorGeometrys = inspectPivot()
        self.DuplicatesShapesOBJ = insepectDuplicatesShapes()
        self.vertexErrorOBJ      = inspectVertex()
        self.hierarchyErrorOBJ   = inspectHierarchyError()
        #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
        def _readResult(OBJList, field, button):
            if len(OBJList) > 0:
                self.turnON(field, button, len(OBJList))
            else:
                self.turnOFF(field, button, len(OBJList))       

        #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
        _readResult(self.DuplacatesNamesOBJ,  self.fld_duplicatesnames,   self.btn_duplicatesnames)
        _readResult(self.defaultNameOBJ,      self.fld_defaultName,       self.btn_defaultName)
        _readResult(self.NoFreeGeometeys,     self.fld_noFreezeGeometeys, self.btn_unFreezeGeometeys)
        _readResult(self.pivotErrorGeometrys, self.fld_pivotError,        self.btn_pivotError)
        _readResult(self.DuplicatesShapesOBJ, self.fld_duplicatesShapes,  self.btn_duplicatesShapes)
        _readResult(self.vertexErrorOBJ,      self.fld_vertexError,       self.btn_vertexError)
        _readResult(self.hierarchyErrorOBJ,   self.fld_hierarchyError,    self.btn_hierarchyError)
        #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-


    def on_btn_duplicatesShapes_clicked(self, args=None):
        if args == None:return
        mc.select(self.DuplicatesShapesOBJ)


    def on_btn_unFreezeGeometeys_clicked(self, args=None):
        if args == None:return
        mc.select(self.NoFreeGeometeys)


    def on_btn_duplicatesnames_clicked(self, args=None):
        if args == None:return
        mc.select(self.DuplacatesNamesOBJ)


    def on_btn_pivotError_clicked(self, args=None):
        if args == None:return
        mc.select(self.pivotErrorGeometrys)

    def on_btn_defaultName_clicked(self, args=None):
        if args == None:return
        mc.select(self.defaultNameOBJ)


    def on_btn_vertexError_clicked(self, args=None):
        if args == None:return
        mc.select(self.vertexErrorOBJ)


    def on_btn_hierarchyError_clicked(self, args=None):
        if args == None:return
        mc.select(self.hierarchyErrorOBJ)







def getGeometrys():
    geometrys = mc.listRelatives(mc.ls(type=('mesh', 'nurbsSurface')), p=True, path=True) or list()
    return geometrys



def inspectDuplicatesNames():
    transforms = string.join(mc.ls(type='transform'))
    Results = re.findall('\S+\|+\S+', transforms)
    return Results



def inspectGeometryAttributes():
    geometrys = getGeometrys()

    Results = []
    for geo in geometrys:
        Values = []

        for attr in ('tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz'):
            Values.append(mc.getAttr('%s.%s'%(geo, attr)))

        if sum(Values) == 3 and Values[-3:] == [1, 1, 1]:
            continue

        if geo in Results:
            continue

        Results.append(geo)

    return Results



def insepectDuplicatesShapes():
    geometrys = getGeometrys()

    Results = []
    for geo in geometrys:
        if len(mc.listRelatives(geo, s=True)) <= 1:
            continue
        if geo in Results:
            continue
        Results.append(geo)

    return Results



def inspectPivot():
    geometrys = getGeometrys()

    Results = []
    for geo in geometrys:
        pivots = mc.xform(geo, q=True, ws=True, rp=True) + mc.xform(geo, q=True, ws=True, sp=True)
        if round(sum(pivots), 4) == 0:
            continue
        if geo in Results:
            continue
        Results.append(geo)

    return Results




def inpectDefaultName():
    geometrys = ' '.join(getGeometrys())
    Results = dict.fromkeys([x[0] for x in re.findall('(((?<=\s)|^)[a-zA-Z]+\d+((?=\s)|$))', geometrys)]).keys()
    return Results




def inspectHierarchyError():
    geometrys = getGeometrys()

    Results = list()
    for geo in geometrys:
        parent = mc.listRelatives(geo, p=True)
        if not parent and geo not in Results:
            Results.append(geo)

    return Results




def inspectVertex():
    geometrys = getGeometrys()
    pointType = {'nurbsSurface':'cv', 'mesh':'vtx'}

    Results = list()
    for geo in geometrys:
        shpType = mc.nodeType(mc.listRelatives(geo, s=True, path=True)[0])

        vertexValues = scriptTool.openMultiarray(mc.getAttr('%s.%s[:]'%(geo, pointType[shpType])))

        if round(sum(vertexValues), 4) == 0:
            continue

        if geo in Results:
            continue

        Results.append(geo)

    return Results