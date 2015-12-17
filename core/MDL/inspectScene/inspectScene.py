#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Fri, 24 Oct 2014 10:45:39
#========================================
import string, re, os.path, checkingModels
import maya.cmds as mc
import maya.OpenMaya as OpenMaya
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
        self.DuplacatesNamesOBJ  = checkingModels.checkingDuplicatesNames()
        self.defaultNameOBJ      = checkingModels.checkingDefaultName()
        self.NoFreeGeometeys     = checkingModels.checkingAttributes()
        self.pivotErrorGeometrys = checkingModels.checkingCenterPoints()
        self.DuplicatesShapesOBJ = checkingModels.checkingDuplacatesShape()
        self.vertexErrorOBJ      = checkingModels.checkingVertex()
        self.hierarchyErrorOBJ   = checkingModels.checkingHiearachy()
        self.historyErrorOBJ     = checkingModels.checkingHistory()
        #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
        def _readResult(mSelectionList, field, button):
            length = mSelectionList.length()
            if length > 0:
                self.turnON(field, button, length)
            else:
                self.turnOFF(field, button, 0)

        #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
        for lst, let, btn in ((self.DuplacatesNamesOBJ,  self.fld_duplicatesnames,   self.btn_duplicatesnames),
                              (self.defaultNameOBJ,      self.fld_defaultName,       self.btn_defaultName),
                              (self.NoFreeGeometeys,     self.fld_noFreezeGeometeys, self.btn_unFreezeGeometeys),
                              (self.pivotErrorGeometrys, self.fld_pivotError,        self.btn_pivotError),
                              (self.DuplicatesShapesOBJ, self.fld_duplicatesShapes,  self.btn_duplicatesShapes),
                              (self.vertexErrorOBJ,      self.fld_vertexError,       self.btn_vertexError),
                              (self.hierarchyErrorOBJ,   self.fld_hierarchyError,    self.btn_hierarchyError),
                              (self.historyErrorOBJ,     self.fld_historyError,      self.btn_historyError)):
            _readResult(lst, let, btn)
        #-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-


    def on_btn_duplicatesShapes_clicked(self, args=None):
        if args == None:return
        OpenMaya.MGlobal.setActiveSelectionList(self.DuplicatesShapesOBJ)


    def on_btn_unFreezeGeometeys_clicked(self, args=None):
        if args == None:return
        OpenMaya.MGlobal.setActiveSelectionList(self.NoFreeGeometeys)


    def on_btn_duplicatesnames_clicked(self, args=None):
        if args == None:return
        OpenMaya.MGlobal.setActiveSelectionList(self.DuplacatesNamesOBJ)


    def on_btn_pivotError_clicked(self, args=None):
        if args == None:return
        OpenMaya.MGlobal.setActiveSelectionList(self.pivotErrorGeometrys)


    def on_btn_defaultName_clicked(self, args=None):
        if args == None:return
        OpenMaya.MGlobal.setActiveSelectionList(self.defaultNameOBJ)


    def on_btn_vertexError_clicked(self, args=None):
        if args == None:return
        OpenMaya.MGlobal.setActiveSelectionList(self.vertexErrorOBJ)


    def on_btn_hierarchyError_clicked(self, args=None):
        if args == None:return
        OpenMaya.MGlobal.setActiveSelectionList(self.hierarchyErrorOBJ)


    def on_btn_historyError_clicked(self, args=None):
        if args == None:return
        OpenMaya.MGlobal.setActiveSelectionList(self.historyErrorOBJ)