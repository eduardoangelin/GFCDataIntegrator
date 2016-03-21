# -*- coding: UTF-8 -*-
'''
Created on 13 de mar de 2016

@author: Angelin
'''

from br.com.dosoftware.gfcdataintegration.Importer.CSV import *
from br.com.dosoftware.gfcdataintegration.worker import *
from br.com.dosoftware.gfcdataintegration.util.SQLServer import *
from br.com.dosoftware.gfcdataintegration.worker.DataFrameTypes import *

if __name__ == '__main__':
    filename = 'PlanoContasContabilTOTVS.csv'
    #print (readCSV(filename, Constantes.delimiter))
    dtCSV = readCSV2PandasDF(filename)
    dtPlanoContas, typePC = specifyDataFramePlanoContas()
    dtCaixaBanco, typeCB = specifyDataFrameCaixaBanco()
    dtSaldoConta, typeSC = specifyDataFrameSaldoConta()
    dtPlanoContas = createPlanoContasDataFrame(dtCSV, dtPlanoContas)
    dtCaixaBanco = createCaixaBancoDataFrame(dtCSV, dtCaixaBanco)
    dtSaldoConta = createSaldoContaDataFrame(dtCSV, dtSaldoConta)
    #print (dtPlanoContas)
    
    content = SQLServer().scriptInsert(dtPlanoContas, typePC)
    WriteFile("PlanoConta.sql", content)
    content = SQLServer().scriptInsert(dtCaixaBanco, typeCB)
    WriteFile("CaixaBanco.sql", content)
    content = SQLServer().scriptInsert(dtSaldoConta, typeSC)
    WriteFile("SaldoConta.sql", content)
    