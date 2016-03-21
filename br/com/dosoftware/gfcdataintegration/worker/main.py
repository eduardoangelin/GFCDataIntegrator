# -*- coding: UTF-8 -*-
'''
Created on 13 de mar de 2016

@author: Angelin
'''

from br.com.dosoftware.gfcdataintegration.Importer.CSV import *
from br.com.dosoftware.gfcdataintegration.worker import *
from br.com.dosoftware.gfcdataintegration.util.SQLServer import *
from br.com.dosoftware.gfcdataintegration.worker.DataFrameTypes import *

def geraPC():
    filename = 'PlanoContasContabilTOTVS.csv'
    dtCSV = readCSV2PandasDF(filename)
    dtPlanoContas, typePC = specifyDataFramePlanoContas()
    dtPlanoContas = createPlanoContasDataFrame(dtCSV, dtPlanoContas)
    content = SQLServer().scriptInsert(dtPlanoContas, typePC)
    WriteFile("PlanoConta.sql", content)
    
def geraCB():
    filename = 'PlanoContasContabilTOTVS.csv'
    dtCSV = readCSV2PandasDF(filename)
    dtCaixaBanco, typeCB = specifyDataFrameCaixaBanco()
    dtCaixaBanco = createCaixaBancoDataFrame(dtCSV, dtCaixaBanco)
    content = SQLServer().scriptInsert(dtCaixaBanco, typeCB)
    WriteFile("CaixaBanco.sql", content)
    
def geraSC():
    filename = 'PlanoContasContabilTOTVS.csv'
    dtCSV = readCSV2PandasDF(filename)
    dtSaldoConta, typeSC = specifyDataFrameSaldoConta()
    dtSaldoConta = createCaixaBancoDataFrame(dtCSV, dtSaldoConta)
    content = SQLServer().scriptInsert(dtSaldoConta, typeSC)
    WriteFile("SaldoConta.sql", content)

def geraPCF():
    filename = 'PlanoContasFinanceiro.csv'
    dtCSV = readCSV2PandasDF(filename)
    print (dtCSV)
    dtPlanoContasFinaceiro, typePCF = specifyDataFramePlanoContasFinanceiro()
    dtPlanoContasFinaceiro = createPlanoContasFinaceiroDataFrame(dtCSV, dtPlanoContasFinaceiro)
    print (dtPlanoContasFinaceiro)
    content = SQLServer().scriptInsert(dtPlanoContasFinaceiro, typePCF)
    print (content)
    WriteFile("PlanoContasFinanceiro.sql", content)
    
if __name__ == '__main__':
    geraPCF()