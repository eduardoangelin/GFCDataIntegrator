# -*- coding: UTF-8 -*-
'''
Created on 13 de mar de 2016

@author: Angelin
'''

from br.com.dosoftware.gfcdataintegration.Importer.CSV import *
from br.com.dosoftware.gfcdataintegration.worker import *
from br.com.dosoftware.gfcdataintegration.util.SQLServer import *

if __name__ == '__main__':
    filename = 'PlanoContasContabilTOTVS.csv'
    #print (readCSV(filename, Constantes.delimiter))
    dtCSV = readCSV2PandasDF(filename)
    dtPlanoContas = specifyDataFramePlanoContas()
    dtPlanoContas = createPlanoContasDataFrame (dtCSV, dtPlanoContas)
    print (dtPlanoContas)
    
    print (SQLServer().scriptInsert(dtPlanoContas))
    