#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 05 May 2015 14:40:15
#========================================
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class Mod_Class(object):
    '''
    '''
    def on_RIG_btn_addGroups_clicked(self, args=None):
        if args == None:return
        import addGroups.addGroups
        addGroups.addGroups.AddGroup()


    def on_RIG_btn_ControlColor_clicked(self, args=None):
        if args==None:return
        import ControlColor
        ControlColor.ColorWindow()


    def on_RIG_btn_makeControlSet_clicked(self, args=None):
        if args == None:return
        import createControlSet.createControlSet
        createControlSet.createControlSet.CreateControlSetUI()


    def on_RIG_btn_MirrorControlShape_clicked(self, args=None):
        if args==None:return
        import mirrorCtlShp.mirrorCtlShp
        mirrorCtlShp.mirrorCtlShp.MirrorControlShp()


    def on_RIG_btn_DynamicControl_clicked(self, args=None):
        if args==None:return
        import DynControl.DynControl
        DynControl.DynControl.DynControl()
