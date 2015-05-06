#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Fri, 24 Oct 2014 10:45:39
#========================================
import string, re, os.path
import maya.cmds as mc
from mpUtils import scriptTool, uiTool
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

OK_ICON      = uiTool.QtGui.QIcon()
DEFAULT_ICON = uiTool.QtGui.QIcon()
IMAGE        = uiTool.QtGui.QPixmap(os.path.join(scriptTool.getScriptPath(), 'icon', 'check.png'))
OK_ICON.addPixmap(IMAGE , uiTool.QtGui.QIcon.Disabled, uiTool.QtGui.QIcon.Off)
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
            con.setIcon(DEFAULT_ICON)
            con.setStyleSheet('QPushButton{border:none;}')            


    def turnON(self, field, button, value=0):
        field.setValue(value)
        field.setStyleSheet('color: rgb(255, 90, 90)')

        button.setEnabled(True)
        button.setText('Select')
        button.setIcon(DEFAULT_ICON)
        button.setStyleSheet('')



    def turnOFF(self, field, button, value=0):
        field.setValue(value)
        field.setStyleSheet('')

        button.setEnabled(False)
        button.setText('')
        button.setIcon(OK_ICON)
        button.setStyleSheet('QPushButton{border:none;}')



    def on_btn_InspectScene_clicked(self, args=None):
        if args == None:return
        self.DuplacatesNamesOBJ  = inspectDuplicatesNames()
        self.defaultNameOBJ      = inpectDefaultName()
        self.NoFreeGeometeys     = inspectGeometryAttributes()
        self.pivotErrorGeometrys = inspectPivot()
        self.DuplicatesShapesOBJ = insepectDuplicatesShapes()


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


def inspectDuplicatesNames():
    transforms = string.join(mc.ls(type='transform'))
    Duplicatesnames = re.findall('\S+\|+\S+', transforms)
    return Duplicatesnames



def inspectGeometryAttributes():
    geometrys   = mc.listRelatives(mc.ls(type=('mesh', 'nurbsSurface')), p=True, path=True) or list()

    u_geometrys = []
    for geo in geometrys:
        Values = []

        for attr in ('tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz'):
            Values.append(mc.getAttr('%s.%s'%(geo, attr)))

        if sum(Values) == 3 and Values[-3:] == [1, 1, 1]:
            continue

        if geo in u_geometrys:
            continue

        u_geometrys.append(geo)

    return u_geometrys



def insepectDuplicatesShapes():
    geometrys   = mc.listRelatives(mc.ls(type=('mesh', 'nurbsSurface')), p=True, path=True) or list()

    u_geometrys = []
    for geo in geometrys:
        if len(mc.listRelatives(geo, s=True)) <= 1:
            continue
        if geo in u_geometrys:
            continue
        u_geometrys.append(geo)

    return u_geometrys



def inspectPivot():
    geometrys   = mc.listRelatives(mc.ls(type=('mesh', 'nurbsSurface')), p=True, path=True) or list()

    u_geometrys = []
    for geo in geometrys:
        pivots = mc.xform(geo, q=True, ws=True, rp=True) + mc.xform(geo, q=True, ws=True, sp=True)
        if round(sum(pivots), 4) == 0:
            continue
        if geo in u_geometrys:
            continue
        u_geometrys.append(geo)

    return u_geometrys



def inpectDefaultName():
    geometrys   = ' '.join(mc.listRelatives(mc.ls(type=('mesh', 'nurbsSurface')), p=True, path=True) or list())
    defaults = dict.fromkeys([x[0] for x in re.findall('(((?<=\s)|^)[a-zA-Z]+\d+((?=\s)|$))', geometrys)]).keys()
    return defaults