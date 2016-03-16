# -*- coding: UTF-8 -*-
'''
Created on 13 de mar de 2016

@author: Angelin
'''

import os

class Config(object):
    '''
    classdocs
    '''
    
    def getCSV_PATH(self):
        return os.path.join(os.getcwd(), 'resources', 'CSV')
    
    def getRoot(self):
        return os.path.dirname(__file__)
if __name__ == '__main__':
    print (Config().getRoot())
    #print (Config().getCSV_PATH())
    
    
 