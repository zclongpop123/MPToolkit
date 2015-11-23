#=============================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Wed, 25 Jun 2014 14:43:02
#=============================================
import sys, os, re, string, shutil, itertools
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

VERSION_PRECISION = 3

def getVersionsFiles(path, fextension=None):
    '''
    get versions and files..
    '''
    if not os.path.isdir(path):
        return

    files = os.listdir(path)
    for f in files:
        if not re.search('\.%s$'%(fextension or '\w+'), f):
            continue

        version = re.search('(?<=v)\d{%d}(?=\.)'%VERSION_PRECISION, f)
        if not version:
            continue

        yield version.group(), os.path.join(path, f)




def getVersions(path, fextension=None):
    '''
    get all of versions..
    '''
    versions = dict(getVersionsFiles(path, fextension)).keys()
    versions.sort(reverse=True, key=lambda x:int(x))
    return versions





def getLastVersion(path, fextension=None):
    '''
    get the last version..
    '''
    versions = getVersions(path, fextension) or [0]

    lastVersion = max([int(v) for v in versions])
    lastVersion = string.zfill(lastVersion, VERSION_PRECISION)

    return lastVersion




def getNewVersion(path, fextension=None):
    '''
    get the new version..
    '''
    lastVersion = int(getLastVersion(path, fextension))
    newVersion = string.zfill(lastVersion+1, VERSION_PRECISION)
    return newVersion




def getVersiondFile(path, version, fextension=None):
    '''
    get the last file fullpath by input version..
    '''
    fileDict = dict(getVersionsFiles(path, fextension))
    filePath = fileDict.get(version, '')
    return filePath




def getLastFile(path, fextension=None):
    '''
    get the last file fullpath..
    '''
    lastVersion = getLastVersion(path, fextension)
    lastFile    = getVersiondFile(path, lastVersion, fextension)
    return lastFile




def getNewFile(path, fname_format='name_v*', fextension=None):
    '''
    build a new version file...
    '''
    filePath = ''
    lastFile = getLastFile(path, fextension)
    if not os.path.isfile(lastFile):
        filePath = os.path.join(path, fname_format.replace('*', string.zfill(1, VERSION_PRECISION)))

    else:
        lastVersion = getLastVersion(path, fextension)
        newVersion  = getNewVersion(path, fextension)

        fname, fextension = os.path.splitext(lastFile)
        filePath = re.sub('%s$'%lastVersion, newVersion, fname) + fextension

    return filePath




def publishFile(src, dst):
    if not os.path.isfile(src):
        return False

    folder = os.path.dirname(dst)
    os.path.isdir(folder) or os.makedirs(folder)

    shutil.copy(src, dst)






def OpenFolder(path):
    if not os.path.isdir(path):
        return
    path = os.path.normpath(path)
    if sys.platform == 'darwin':
        os.system('open %s'%path)
    else:
        os.system('explorer.exe %s'%path)
