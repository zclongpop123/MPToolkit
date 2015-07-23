#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 05 May 2015 14:40:15
#========================================
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
class Mod_Class(object):
    '''
    '''
    def on_RIG_btn_LatticeWeight_clicked(self, args=None):
        if args==None:return
        import latticeWeightsTool
        latticeWeightsTool.latticeWeightTool()

    def on_RIG_btn_BlendShapeWeightTool_clicked(self, args=None):
        if args==None:return
        import blendShapeWeights.blendShapeWeights
        blendShapeWeights.blendShapeWeights.BlendShapeWeightUI()    


    def on_RIG_btn_copyClusterWeights_clicked(self, args=None):
        if args==None:return
        import MirrorClusterWeights.MirrorClusterWeights
        MirrorClusterWeights.MirrorClusterWeights.ClusterWeightsUI()    


    def on_RIG_btn_convertSkin_clicked(self, args=None):
        if args==None:return
        import transSkinWeightsToCluster.transWeights
        transSkinWeightsToCluster.transWeights.transWeightsUI()        


    def on_RIG_btn_WeightsTool_clicked(self, args=None):
        if args==None:return
        import weightsTool.weightsTool
        weightsTool.weightsTool.WeightsTool()      


    def on_RIG_btn_CopyBlendShapeWeights_clicked(self, args=None):
        if args==None:return
        import CopyBlendShapeWeights.CopyBlendShapeWeights
        CopyBlendShapeWeights.CopyBlendShapeWeights.CopyBlendShapeWeightsUI()        


    def on_RIG_btn_EditBlendShapeWeights_clicked(self, args=None):
        if args==None:return
        import blendShapeWeightsTool.blendShapeWeights
        blendShapeWeightsTool.blendShapeWeights.BlendShapeWeightsUI()
    
    
    def on_RIG_btn_InvertBlendShapeWeights_clicked(self, args=None):
        if args==None:return
        import invertBlendShapeWeights.blendShapeWeights
        invertBlendShapeWeights.blendShapeWeights.BlendShapeWeightUI()