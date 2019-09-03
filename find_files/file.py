'''
Created on 30-Aug-2019

@author: elango

'''

import os, fnmatch

#class FindPath(object):
__all__ = ["findFileByName","findAllFileByName","findFileByPattern"]
    
    # constructor
def findFileByName(name, path):
    
    """
    findFileByName(name, path)

    findFileByName; Search the file by using name of the file in directory.
    Once using name indicates the file name and path indicates the directory where
    you want to search. 
    findFileByName('demo.xml', '/path/to/dir')
    
    """
    for root, _dirs_, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
        

def findAllFileByName(name, path):
    
    """
    findAllFileByName(name, path)

    findAllFileByName; Search the all files by using name of the file in directory.
    Once using name indicates the file name and path indicates the directory where
    you want to search. 
    findAllFileByName('demo.xml', '/path/to/dir')
    
    """
    result = []
    for root, _dirs_, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result


def findFileByPattern(pattern, path):
 
    """
    findFileByPattern(name, path)

    findFileByPattern; Search the file by using extension of the file in directory.
    Once using pattern indicates the file extension and path indicates the directory where
    you want to search. 
    findFileByPattern('*.xml', '/path/to/dir')
    
    """
    result = []
    for root, _dirs_, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result
    