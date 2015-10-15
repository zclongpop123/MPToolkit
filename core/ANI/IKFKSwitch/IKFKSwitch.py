#=============================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 29 Jul 2014 09:29:32
#=============================================
import math, re, os
import maya.cmds as mc
from mpUtils import uiTool, scriptTool, mayaTool, mathTool
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#- Refresh Characters                                           +
#- Guess Character Type                                         +
#- Left arm, Right arm, Left leg, Right leg                     +
#- Left foreleg, Right foreleg, Left hindleg, Right hindleg     +
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


Uiwnd, UiClass = uiTool.loadUi(os.path.join(scriptTool.getScriptPath(), 'IKFKSwitch.ui'))
class IKFKSwitch(Uiwnd, UiClass):
    def __init__(self, parent =uiTool.getMayaWindow()):
        if uiTool.windowExists('DDikfkSwitchWindow'):
            return    

        super(IKFKSwitch, self).__init__(parent)
        self.setupUi(self)
        self.show()
        #--------
        self.on_actionRefreshCharacter_triggered(True)


    def on_actionRefreshCharacter_triggered(self, args=None):
        if args==None:return
        self.Controls = ' '.join(mc.ls())

        referenceCharacters = [mc.file(f, q=True, ns=True) for f in mc.file(q=True, r=True) if re.search('\Wcharacter\W', f)]
        self.CharacterComboBox.clear()
        for ns in referenceCharacters:
            self.CharacterComboBox.addItem(ns)



    def on_actionCurrentCharacterChanged_triggered(self, args=None):
        if args==None:return
        nameSpace = str(self.CharacterComboBox.currentText())
        if re.search('%s\S*%s'%(nameSpace, 'L_arm_mod_0'), self.Controls):
            self.radioButton_A.setChecked(True)
        else:
            self.radioButton_B.setChecked(True)

    #----------------------------------------------------------------------------------------------------------------
    @mayaTool.undo_decorator
    def on_actionLeftArmSwitch_triggered(self, args=None):
        if args==None:return
        namespace = str(self.CharacterComboBox.currentText())
        side = 'L'
        if mc.getAttr('%s:%s_armIKFKSwitch_ctl_0.FKIKBlend'%(namespace, side)) == 0:
            args = (('_armshoulderIK_jnt_0', '_armshoulderFK_ctl_0'),
                    ('_armelbowIK_jnt_0',    '_armelbowFK_ctl_0'),
                    ('_armwristIK_jnt_0',    '_armwristFK_ctl_0'))

            for src, dst in args:
                ps = mc.xform('%s:%s%s'%(namespace, side, src), q=True, ws=True, t=True)
                ro = mc.xform('%s:%s%s'%(namespace, side, src), q=True, ws=True, ro=True)

                mc.xform('%s:%s%s'%(namespace, side, dst), ws=True, t=ps)
                mc.xform('%s:%s%s'%(namespace, side, dst), ws=True, ro=ro)

            mc.setAttr('%s:%s_armIKFKSwitch_ctl_0.FKIKBlend'%(namespace, side), 1)

        else:
            args = (('_armArmIK_ctlaim_0', '_armArmIK_ctl_0'),)

            for src, dst in args:
                ps = mc.xform('%s:%s%s'%(namespace, side, src), q=True, ws=True, t=True)
                ro = mc.xform('%s:%s%s'%(namespace, side, src), q=True, ws=True, ro=True)

                mc.xform('%s:%s%s'%(namespace, side, dst), ws=True, t=ps)
                mc.xform('%s:%s%s'%(namespace, side, dst), ws=True, ro=ro)            

            pole_ps = mathTool.getPoleVectorPosition('%s:%s%s'%(namespace, side, '_armUpTwist1_bnd_0'), '%s:%s%s'%(namespace, side,'_armLowTwist1_bnd_0'), '%s:%s%s'%(namespace, side,'_armwrist_bnd_0'))
            mc.xform('%s:%s%s'%(namespace, side, '_armArmPole_ctl_0'), ws=True, t=pole_ps)

            mc.setAttr('%s:%s_armIKFKSwitch_ctl_0.FKIKBlend'%(namespace, side), 0)


    @mayaTool.undo_decorator 
    def on_actionRightArmSwitch_triggered(self, args=None):
        if args==None:return
        namespace = str(self.CharacterComboBox.currentText())
        side = 'R'
        if mc.getAttr('%s:%s_armIKFKSwitch_ctl_0.FKIKBlend'%(namespace, side)) == 0:
            args = (('_armshoulderIK_jnt_0', '_armshoulderFK_ctl_0'),
                    ('_armelbowIK_jnt_0',    '_armelbowFK_ctl_0'),
                    ('_armwristIK_jnt_0',    '_armwristFK_ctl_0'))

            for src, dst in args:
                ps = mc.xform('%s:%s%s'%(namespace, side, src), q=True, ws=True, t=True)
                ro = mc.xform('%s:%s%s'%(namespace, side, src), q=True, ws=True, ro=True)

                mc.xform('%s:%s%s'%(namespace, side, dst), ws=True, t=ps)
                mc.xform('%s:%s%s'%(namespace, side, dst), ws=True, ro=ro)

            pole_ps = mathTool.getPoleVectorPosition('%s:%s%s'%(namespace, side, '_armUpTwist1_bnd_0'), '%s:%s%s'%(namespace, side,'_armLowTwist1_bnd_0'), '%s:%s%s'%(namespace, side,'_armwrist_bnd_0'))
            mc.xform('%s:%s%s'%(namespace, side, '_armArmPole_ctl_0'), ws=True, t=pole_ps)

            mc.setAttr('%s:%s_armIKFKSwitch_ctl_0.FKIKBlend'%(namespace, side), 1)

        else:
            args = (('_armArmIK_ctlaim_0', '_armArmIK_ctl_0'),)

            for src, dst in args:
                ps = mc.xform('%s:%s%s'%(namespace, side, src), q=True, ws=True, t=True)
                ro = mc.xform('%s:%s%s'%(namespace, side, src), q=True, ws=True, ro=True)

                mc.xform('%s:%s%s'%(namespace, side, dst), ws=True, t=ps)
                mc.xform('%s:%s%s'%(namespace, side, dst), ws=True, ro=ro)

            mc.setAttr('%s:%s_armIKFKSwitch_ctl_0.FKIKBlend'%(namespace, side), 0)



    @mayaTool.undo_decorator    
    def on_actionLeftLegSwitch_triggered(self, args=None):
        if args==None:return
        namespace = str(self.CharacterComboBox.currentText())
        side = 'L'
        if mc.getAttr('%s:%s_legIKFKSwitch_ctl_0.FKIKBlend'%(namespace, side)) == 0:
            args = (('_leghip_jnt_0',    '_leghip_ctl_0'),
                    ('_leglegIK_jnt_0',  '_leglegFK_ctl_0'),
                    ('_legkneeIK_jnt_0',  '_legkneeFK_ctl_0'),
                    ('_legankleFK_ctlaim_0', '_legankleFK_ctl_0'),#('_legankleIK_jnt_0', '_legankleFK_ctl_0'),
                    ('_legsoleFK_ctlaim_0',  '_legsoleFK_ctl_0')) #('_legsoleIK_jnt_0',  '_legsoleFK_ctl_0'))

            for src, dst in args:
                ps = mc.xform('%s:%s%s'%(namespace, side, src), q=True, ws=True, t=True)
                ro = mc.xform('%s:%s%s'%(namespace, side, src), q=True, ws=True, ro=True)

                mc.xform('%s:%s%s'%(namespace, side, dst), ws=True, t=ps)
                mc.xform('%s:%s%s'%(namespace, side, dst), ws=True, ro=ro)

            mc.setAttr('%s:%s_legIKFKSwitch_ctl_0.FKIKBlend'%(namespace, side), 1)

        else:
            args = (('_legLegIK_ctlaim_0', '_legLegIK_ctl_0'),)

            for src, dst in args:
                ps = mc.xform('%s:%s%s'%(namespace, side, src), q=True, ws=True, t=True)
                ro = mc.xform('%s:%s%s'%(namespace, side, src), q=True, ws=True, ro=True)

                mc.xform('%s:%s%s'%(namespace, side, dst), ws=True, t=ps)
                mc.xform('%s:%s%s'%(namespace, side, dst), ws=True, ro=ro)      

            pole_ps = mathTool.getPoleVectorPosition('%s:%s%s'%(namespace, side, '_legUpTwist1_bnd_0'), '%s:%s%s'%(namespace, side,'_legLowTwist1_bnd_0'), '%s:%s%s'%(namespace, side,'_legankle_bnd_0'))
            mc.xform('%s:%s%s'%(namespace, side, '_legLegPole_ctl_0'), ws=True, t=pole_ps)       

            mc.setAttr('%s:%s_legIKFKSwitch_ctl_0.FKIKBlend'%(namespace, side), 0)     


    @mayaTool.undo_decorator   
    def on_actionRightLegSwitch_triggered(self, args=None):
        if args==None:return
        namespace = str(self.CharacterComboBox.currentText())
        side = 'R'
        if mc.getAttr('%s:%s_legIKFKSwitch_ctl_0.FKIKBlend'%(namespace, side)) == 0:
            args = (('_leghip_jnt_0',    '_leghip_ctl_0'),
                    ('_leglegIK_jnt_0',  '_leglegFK_ctl_0'),
                    ('_legkneeIK_jnt_0',  '_legkneeFK_ctl_0'),
                    ('_legankleFK_ctlaim_0', '_legankleFK_ctl_0'),#('_legankleIK_jnt_0', '_legankleFK_ctl_0'),
                    ('_legsoleFK_ctlaim_0',  '_legsoleFK_ctl_0')) #('_legsoleIK_jnt_0',  '_legsoleFK_ctl_0'))

            for src, dst in args:
                ps = mc.xform('%s:%s%s'%(namespace, side, src), q=True, ws=True, t=True)
                ro = mc.xform('%s:%s%s'%(namespace, side, src), q=True, ws=True, ro=True)

                mc.xform('%s:%s%s'%(namespace, side, dst), ws=True, t=ps)
                mc.xform('%s:%s%s'%(namespace, side, dst), ws=True, ro=ro)

            pole_ps = mathTool.getPoleVectorPosition('%s:%s%s'%(namespace, side, '_legUpTwist1_bnd_0'), '%s:%s%s'%(namespace, side,'_legLowTwist1_bnd_0'), '%s:%s%s'%(namespace, side,'_legankle_bnd_0'))
            mc.xform('%s:%s%s'%(namespace, side, '_legLegPole_ctl_0'), ws=True, t=pole_ps)            

            mc.setAttr('%s:%s_legIKFKSwitch_ctl_0.FKIKBlend'%(namespace, side), 1)

        else:
            args = (('_legLegIK_ctlaim_0', '_legLegIK_ctl_0'),)

            for src, dst in args:
                ps = mc.xform('%s:%s%s'%(namespace, side, src), q=True, ws=True, t=True)
                ro = mc.xform('%s:%s%s'%(namespace, side, src), q=True, ws=True, ro=True)

                mc.xform('%s:%s%s'%(namespace, side, dst), ws=True, t=ps)
                mc.xform('%s:%s%s'%(namespace, side, dst), ws=True, ro=ro)      

            mc.setAttr('%s:%s_legIKFKSwitch_ctl_0.FKIKBlend'%(namespace, side), 0)     


    @mayaTool.undo_decorator
    def on_actionLeftForeLegSwitch_triggered(self, args=None):
        pass


    @mayaTool.undo_decorator  
    def on_actionRightForeLegSwitch_triggered(self, args=None):
        pass


    @mayaTool.undo_decorator    
    def on_actionLeftHindLegSwitch_triggered(self, args=None):
        pass


    @mayaTool.undo_decorator   
    def on_actionRightHindLegSwitch_triggered(self, args=None):
        pass