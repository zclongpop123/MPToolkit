#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 05 May 2015 14:40:15
#========================================
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class Mod_Class(object):
    '''
    '''
    def on_RIG_btn_NameTool_clicked(self, args=None):
        if args == None:return
        import nameTool.nameToolCmds
        nameTool.nameToolCmds.NameUI()    


    def on_RIG_btn_AddIKFKSwitch_clicked(self, args=None):
        if args==None:return
        import IKFKSwitch 
        IKFKSwitch .addIKFKSwitch()    


    def on_RIG_btn_MakeHeadStreatch_clicked(self, args=None):
        if args==None:return
        import HeadStreatch.HeadStreatchTool
        HeadStreatch.HeadStreatchTool.HeadStreatchUI()


    def on_RIG_btn_AddPalmJoint_clicked(self, args=None):
        if args==None:return
        import addPalmBindJoint
        addPalmBindJoint.addPalmBindJoint()    