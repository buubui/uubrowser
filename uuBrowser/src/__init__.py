import os
BASEDIR=os.path.dirname(__file__)
__version__='0.1 pre alpha'
__author__={'buubui':'bhlbuu@apcs.vn'}

sep=os.sep
def generatePath(path):
    if path:
        return path.replace('/',sep)
def pathFromBase(path):
    return generatePath(BASEDIR+path)