#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 12 Aug 2014 16:01:28
#========================================

#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class Mdl_Class(object):
    '''
    Modeling team classes...
    '''
    def on_MDL_btn_inspect_clicked(self, args=None):
        if args is None:return
        import inspectScene.inspectScene
        inspectScene.inspectScene.InspectSceneUI()


    def on_MDL_btn_findCoincidentGeometry_clicked(self, args=None):
        if args == None:return
        import findCoincidentGeometry.findCoincidentGeometryUI
        findCoincidentGeometry.findCoincidentGeometryUI.findCoincidentGeometryUI()


    def on_MDL_btn_ReplaceUV_clicked(self, args=None):
        if args == None:return
        import ReplaceUV.ReplaceUV
        ReplaceUV.ReplaceUV.ReplaceUV()
