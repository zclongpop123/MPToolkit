#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 05 May 2015 14:40:15
#========================================
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class Mod_Class(object):
    '''
    '''
    def on_RIG_btn_SetToesDrivenKey_clicked(self, args=None):
        if args==None:return
        import SetDrivenKeysforToes
        SetDrivenKeysforToes.SetDrivenKeyforToes()


    def on_RIG_btn_MirrorDrivenkey_clicked(self, args=None):
        if args==None:return
        import mirrorSDK
        mirrorSDK.MirrorSetDrivenKey()


    def on_RIG_btn_QuickSDKA_clicked(self, args=None):
        if args==None:return
        import quickSDKTool.quickSDKTool
        quickSDKTool.quickSDKTool.quickSDK()


    def on_RIG_btn_QuickSDKB_clicked(self, args=None):
        if args==None:return
        import quickSetDrivenKey.quickSetDrivenKey
        quickSetDrivenKey.quickSetDrivenKey.QuickSetDrivenKey()
