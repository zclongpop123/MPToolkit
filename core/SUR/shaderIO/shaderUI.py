#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 28 Apr 2015 09:40:23
#========================================
from mpUtils import scriptTool, uiTool
import os.path, shaderCore
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
windowClass, baseClass = uiTool.loadUi(os.path.join(scriptTool.getScriptPath(), 'shaderUI.ui'))

class ShaderUI(windowClass, baseClass):
    def __init__(self, parent=uiTool.getMayaWindow()):
        #-----------------------------------------------------
        if uiTool.windowExists('shaderIOToolUI'):return
        #-----------------------------------------------------   
        super(ShaderUI, self).__init__(parent)
        self.setupUi(self)
        self.show()


    def on_btn_export_clicked(self, args=None):
        if args == None:return
        shaderCore.exportGeometryShader()


    def on_btn_import_clicked(self, args=None):
        if args == None:return    
        shaderCore.importGeometryShader()