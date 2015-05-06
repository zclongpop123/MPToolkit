#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 12 Aug 2014 16:01:28
#========================================
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class Ani_Class(object):
    '''
    Animation team classes...
    '''
    def on_ANI_btn_ControlSelecter_clicked(self, args=None):
        if args is None:return
        import ControlSelecter.ControlSelecterUI
        ControlSelecter.ControlSelecterUI.ControlSelecterWnd()


    def on_ANI_btn_IKFKSwitch_clicked(self, args=None):
        if args is None:return
        import IKFKSwitch.IKFKSwitch
        IKFKSwitch.IKFKSwitch.IKFKSwitch()


    def on_ANI_btn_Tpose_clicked(self, args=None):
        if args is None:return


    def on_ANI_btn_FixAnim_clicked(self, args=None):
        if args is None:return


    def on_ANI_btn_animSceneReader_clicked(self, args=None):
        if args is None:return