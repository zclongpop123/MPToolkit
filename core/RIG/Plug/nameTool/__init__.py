#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Thu, 07 May 2015 10:48:25
#========================================
import sys
from mpUtils import scriptTool
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
thisPath = scriptTool.getScriptPath()
thisPath in sys.path or sys.path.append(thisPath)
