#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 05 May 2015 14:40:15
#========================================
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class Mod_Class(object):
    '''
    '''
    def on_RIG_btn_ReBuildeTargents_clicked(self, args=None):
        if args==None:return
        import buildTargents.buildTargents
        buildTargents.buildTargents.BuildTargents()


    def on_RIG_btn_ShapeBuilder_clicked(self, args=None):
        if args==None:return
        import ShapeBuilder.ShapeBuilderUI
        ShapeBuilder.ShapeBuilderUI.ShapeBuilderUI()


    def on_RIG_btn_fixShapeTool_clicked(self, args=None):
        if args==None:return
        import FixShape.FixShape
        FixShape.FixShape.FixShapeUI()
