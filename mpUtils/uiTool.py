#=============================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Thu, 03 Jul 2014 16:35:02
#=============================================
import sip, re, os.path, sip, scriptTool, maya.OpenMayaUI
from PyQt4 import QtCore, QtGui, uic
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

def wrapInstance(widget):
    if isinstance(widget, basestring):
        widget = maya.OpenMayaUI.MQtUtil.findWindow(widget)
    return sip.wrapinstance(long(widget), QtCore.QObject)



def getMayaWindow():
    '''
    return maya window by Qt object..
    '''
    widget = maya.OpenMayaUI.MQtUtil.mainWindow()
    if widget:
        return wrapInstance(widget)



def loadUi(uiPath):
    '''
    read an ui file, get two classes to return..
    '''
    return uic.loadUiType(uiPath)



def windowExists(name):
    '''
    get named window, if window exists, return true; if not, return false..
    '''
    widget = maya.OpenMayaUI.MQtUtil.findWindow(name)
    if not widget:
        return False

    wnd = wrapInstance(widget)
    wnd.showNormal()
    wnd.activateWindow()

    return True




def getChildrenWindows(parent):
    '''
    get object's children windows..
    '''
    if not parent:return

    for child in parent.children():
        if not hasattr(child, 'isWindow'):
            continue

        if not child.isWindow():
            continue

        yield child





def cleanChildrenWindows(parent, delete=False):
    '''
    delete window's child window...
    '''
    if not parent:return

    for child in getChildrenWindows(parent):
        if not re.match('rigBuilder', child.__module__):
            continue
        child.close()
        if not delete:continue
        child.deleteLater()