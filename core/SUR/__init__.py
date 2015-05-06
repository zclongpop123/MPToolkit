#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Thu, 30 Apr 2015 09:47:27
#========================================
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class Sur_Class(object):
    '''
    Surface shader team classes...
    '''
    def on_SUR_btn_ShaderIO_clicked(self, args=None):
        if args is None:return
        import shaderIO.shaderUI
        shaderIO.shaderUI.ShaderUI()    