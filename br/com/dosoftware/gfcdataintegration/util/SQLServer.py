# -*- coding: UTF-8 -*-
'''
Created on 13 de mar de 2016

@author: Angelin
'''
from br.com.dosoftware.gfcdataintegration.util.Constantes import Constantes
import numpy as np

class SQLServer(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def applyType(self, value, format):
        if (format == Constantes.TYPE_STR):
            return "'{}'".format(value)
        if (format == Constantes.TYPE_DATE):
            return "'{}'".format(value)
        if (format == Constantes.TYPE_QUERY):
            return "({})".format(value)
        return str(value)
    
    def scriptInsert(self, tableName, df, dictTypes, withGO = True):
        columns = list(df.columns.values)
        cmd = ''
        for idx, row in df.iterrows():
            cmd += 'INSERT INTO '+ tableName + ' ('
            for j in columns:
                cmd += str(j)+', '
            cmd = cmd[0:-2] + ") VALUES ("
            for j in columns:
                if (row[j] != None and (str(row[j]) != 'nan')):
                    value = self.applyType(row[j], dictTypes[j])
                else:
                    value = 'NULL'
                cmd += value+", "
            cmd = cmd[0:-2] + ")\n"
            if (withGO):
                cmd += 'GO\n'
        return cmd
    
    def scriptExecute(self, procedureName, df, dictTypes, withGO = True):
        columns = list(df.columns.values)
        print (columns)
        print (df)
        cmd = ''
        for idx, row in df.iterrows():
            cmd += 'EXECUTE '+ procedureName + ' '
            for j in columns:
                if (row[j] != None and (str(row[j]) != 'nan')):
                    value = self.applyType(row[j], dictTypes[j])
                else:
                    value = 'NULL'
                cmd += value+", "
            cmd = cmd[0:-2] + "\n"
            if (withGO):
                cmd += 'GO\n'
        return cmd
    
    def getID(self, idCTA, table, column, value):
        result = "SELECT "+ idCTA +" FROM "+table+" WHERE " + column + " LIKE '" + value + "'"
        return result

    def getIDCentroCustoByNome(self, value):
        result = self.getID("ID", "CENTROCUSTO", "CCUST", value)
        return result
    
    def getIDPlanoContasByCodigo(self, value):
        result = self.getID("ID", "PLANOCONTAS", "COD_CTA", value)
        return result
    
    def getIDPlanoContasByConta(self, value):
        result = self.getID("ID", "PLANOCONTAS", "CTA", value)
        return result
    