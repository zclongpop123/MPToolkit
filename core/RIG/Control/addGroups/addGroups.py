#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 05 May 2015 11:39:42
#========================================
import os.path, pymel.core
import maya.cmds as mc
from PyQt4 import QtGui
from mpUtils import scriptTool, uiTool
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

windowClass, baseClass = uiTool.loadUi(os.path.join(scriptTool.getScriptPath(), 'addGroups.ui'))
class AddGroup(windowClass, baseClass):
    '''
    user control pannel...
    '''
    def __init__(self, parent=uiTool.getMayaWindow()):
        if uiTool.windowExists('addGroupWindow'):
            return 

        super(AddGroup, self).__init__(parent)
        self.setupUi(self)
        self.show()

    def on_btn_append_clicked(self, args=None):
        if args == None:return
        lineEdit = QtGui.QLineEdit(self.scrollArea)
        font = QtGui.QFont()
        font.setPointSize(10)
        lineEdit.setFont(font)
        lineEdit.setMinimumHeight(25)
        self.verticalLayout_4.insertWidget(self.verticalLayout_4.count()-1, lineEdit)
        lineEdit.setFocus()


    def on_btn_remove_clicked(self, args=None):
        if args == None:return        
        LineEdits = self.scrollArea.findChildren(QtGui.QLineEdit)
        if len(LineEdits) == 1:return
        LineEdits.pop().deleteLater()
        LineEdits[-1].setFocus()



    def on_btn_add_clicked(self, args=None):
        if args == None:return

        search = str(self.let_Search.text())
        selObj = mc.ls(sl=True)
        nameLabels = [str(x.text()) for x in self.scrollArea.findChildren(QtGui.QLineEdit)]
        nameLabels.reverse()

        for obj in selObj:
            for replace in nameLabels:
                if obj.strip() == '':continue
                addGroup(obj, search, replace)




def addGroup(obj, search, replace):
    transform = pymel.core.createNode('transform', n=obj.replace(search, replace))
    mc.delete(mc.parentConstraint(obj, transform.name()))

    objParent = mc.listRelatives(obj, p=True, path=True)
    if objParent:
        mc.parent(transform.name(), objParent)
    mc.parent(obj, transform.name())