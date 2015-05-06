#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Wed, 29 Apr 2015 16:13:12
#========================================
import sys, os.path, mpUtils.scriptTool
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
scriptPath = os.path.normcase(mpUtils.scriptTool.getScriptPath())
qt_resource_path = os.path.join(scriptPath, 'resource')

scriptPath in sys.path or sys.path.append(scriptPath)
qt_resource_path in sys.path or sys.path.append(qt_resource_path)