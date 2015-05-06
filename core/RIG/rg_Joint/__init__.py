#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 05 May 2015 14:40:15
#========================================
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class Mod_Class(object):
    '''
    '''
    def on_RIG_btn_MakeJointsOnCurve_clicked(self, args=None):
        if args==None:return
        import makeAttachJoints.makeAttachJoints 
        makeAttachJoints.makeAttachJoints.makeAttachJoints()    



    def on_RIG_btn_makeRotateInfo_clicked(self, args=None):
        if args==None:return
        import makeRotateInfo
        makeRotateInfo.makeRotateInfo()    