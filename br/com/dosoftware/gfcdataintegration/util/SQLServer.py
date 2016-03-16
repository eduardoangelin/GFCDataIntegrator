# -*- coding: UTF-8 -*-
'''
Created on 13 de mar de 2016

@author: Angelin
'''

class SQLServer(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def scriptInsert(self, df, withGO = True):
        columns = list(df.columns.values)
        cmd = ''
        for idx, row in df.iterrows():
            #print ('Linha: '+str(idx))
            cmd += 'INSERT INTO ('
            for j in columns:
                cmd += str(j)+', '
            cmd = cmd[0:-2] + ") VALUES ('"
            for j in columns:
                cmd += str(row[j])+"', '"
            cmd = cmd[0:-3] + ")\n"
            if (withGO):
                cmd += 'GO\n'
            #print (cmd)
        return cmd
    