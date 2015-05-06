#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Wed, 29 Apr 2015 10:09:50
#========================================
import os.path
from mpUtils import scriptTool, uiTool
from core    import MDL, SUR, RIG, ANI, LGT, FX, CMP
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
windowClass, baseClass = uiTool.loadUi(os.path.join(scriptTool.getScriptPath(), 'MPToolkitUI.ui'))
class MPToolkitUI(windowClass, baseClass, MDL.Mdl_Class, SUR.Sur_Class, RIG.Rig_Class, ANI.Ani_Class, LGT.Lgt_Class, FX.Fx_Class, CMP.Cmp_Class):
    '''
    '''
    def __init__(self, parent=uiTool.getMayaWindow()):
        #-----------------------------------------------------
        if uiTool.windowExists('magicpowerToolKit'):return
        #-----------------------------------------------------          
        super(MPToolkitUI, self).__init__(parent)
        self.setupUi(self)
        self.__initUI()
        self.show()


    def __initUI(self):
        #- hide tabwidget tabbar...
        self.tabWidget.tabBar().setVisible(False)
        
        #- connect all of radiobuttons...
        self.__buttonGroup = uiTool.QtGui.QButtonGroup()
        for i, rdn in enumerate(self.wgt_rdnbox.findChildren(uiTool.QtGui.QRadioButton)):
            self.__buttonGroup.addButton(rdn, i)
        uiTool.QtCore.QObject.connect(self.__buttonGroup, uiTool.QtCore.SIGNAL('buttonClicked(int)'), self.tabWidget.setCurrentIndex)