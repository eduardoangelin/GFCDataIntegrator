# -*- coding: UTF-8 -*-
'''
Created on 13 de mar de 2016

@author: Angelin
'''

from br.com.dosoftware.gfcdataintegration.Importer.CSV import *
from br.com.dosoftware.gfcdataintegration.worker import *
from br.com.dosoftware.gfcdataintegration.util.SQLServer import *
from br.com.dosoftware.gfcdataintegration.worker.DataFrameTypes import *

def geraPC(filename = 'PlanoContasContabilCCEduardo.csv'):
    tableName = "PLANOCONTAS"
    dtCSV = readCSV2PandasDF(filename)
    dtPlanoContas, typePC = specifyDataFramePlanoContas()
    dtPlanoContas = createPlanoContasDataFrame(dtCSV, dtPlanoContas)
    content = SQLServer().scriptInsert(tableName, dtPlanoContas, typePC)
    WriteFile(tableName+".sql", content)
    return content
    
def geraCB(filename = 'PlanoContasContabilCCEduardo.csv'):
    tableName = "CAIXABANCO"
    dtCSV = readCSV2PandasDF(filename)
    dtCaixaBanco, typeCB = specifyDataFrameCaixaBanco()
    dtCaixaBanco = createCaixaBancoDataFrame(dtCSV, dtCaixaBanco)
    content = SQLServer().scriptInsert(tableName, dtCaixaBanco, typeCB)
    WriteFile(tableName+".sql", content)
    return content
    
def geraCF(filename = 'PlanoContasContabilCCEduardo.csv'):
    tableName = "CLIENTEFORNECEDOR"
    dtCSV = readCSV2PandasDF(filename)
    dtClienteFornecedor, typeCF = specifyDataFrameClienteFornecedor()
    dtClienteFornecedor = createClienteFornecedorDataFrame(dtCSV, dtClienteFornecedor)
    content = SQLServer().scriptInsert(tableName, dtClienteFornecedor, typeCF)
    WriteFile(tableName+".sql", content)
    return content
    
def geraRE(filename = 'PlanoContasContabilCCEduardo.csv'):
    tableName = "RESULTADO"
    dtCSV = readCSV2PandasDF(filename)
    dtResultado, typeRES = specifyDataFrameResultado()
    dtResultado = createResultadoDataFrame(dtCSV, dtResultado, Constantes.RES)
    content = SQLServer().scriptInsert(tableName, dtResultado, typeRES)
    WriteFile(tableName+".sql", content)
    return content
    
def geraJUR(filename = 'PlanoContasContabilCCEduardo.csv'):
    tableName = "JUROS"
    dtCSV = readCSV2PandasDF(filename)
    dtResultado, typeJUR = specifyDataFrameResultado()
    dtResultado = createResultadoDataFrame(dtCSV, dtResultado, Constantes.JUR)
    content = SQLServer().scriptInsert(tableName, dtResultado, typeJUR)
    WriteFile(tableName+".sql", content)
    return content
    
def geraDESC(filename = 'PlanoContasContabilCCEduardo.csv'):
    tableName = "DESCONTO"
    dtCSV = readCSV2PandasDF(filename)
    dtResultado, typeDESC = specifyDataFrameResultado()
    dtResultado = createResultadoDataFrame(dtCSV, dtResultado, Constantes.DESC)
    content = SQLServer().scriptInsert(tableName, dtResultado, typeDESC)
    WriteFile(tableName+".sql", content)
    return content
    
def geraSC(filename = 'PlanoContasContabilCCEduardo.csv'):
    tableName = "SALDOCONTAS"
    dtCSV = readCSV2PandasDF(filename)
    dtSaldoConta, typeSC = specifyDataFrameSaldoConta()
    dtSaldoConta = createSaldoContaDataFrame(dtCSV, dtSaldoConta)
    content = SQLServer().scriptInsert(tableName, dtSaldoConta, typeSC)
    WriteFile(tableName+".sql", content)
    return content

def geraPCF(filename = 'PlanoContasFinanceiroEduardo.csv'):
    tableName = "PLANOCONTASFINANCEIRO"
    dtCSV = readCSV2PandasDF(filename)
    dtPlanoContasFinaceiro, typePCF = specifyDataFramePlanoContasFinanceiro()
    dtPlanoContasFinaceiro = createPlanoContasFinaceiroDataFrame(dtCSV, dtPlanoContasFinaceiro)
    dtPlanoContasFinaceiro = addMovimentacaoTransitoria(dtCSV, dtPlanoContasFinaceiro)
    dtPlanoContasFinaceiro = addDisponibilidadeFinal(dtCSV, dtPlanoContasFinaceiro)
    content = SQLServer().scriptInsert(tableName, dtPlanoContasFinaceiro, typePCF)
    WriteFile(tableName+".sql", content)
    return content
    
def geraPCCompleto(filenameContabil, filenameFinanceiro):
    result = ''
    result += geraPC(filenameContabil)
    result += geraCB(filenameContabil)
    result += geraCF(filenameContabil)
    result += geraRE(filenameContabil)
    result += geraJUR(filenameContabil)
    result += geraDESC(filenameContabil)
    result += geraSC(filenameContabil)
    result += geraPCF(filenameFinanceiro)
    return result
    
def geraLancamento(filename):
    procedureName = "SP_GERAMOVIMENTO_AUXILIAR"
    dtCSV = readCSV2PandasDF(filename)
    dtGeraMovimento, typeMOV = specifyDataFrameGeraMovimento()
    dtGeraMovimento = createGeraMovimentoDataFrame(dtCSV, dtGeraMovimento)
    content = SQLServer().scriptExecute(procedureName, dtGeraMovimento, typeMOV)
    WriteFile(filename.split('.')[0]+".sql", content)
    return content


if __name__ == '__main__':
    #filenameContabil = 'PlanoContasContabilCCEduardo.csv'
    #filenameFinanceiro = 'PlanoContasFinanceiroCCEduardo.csv'
    #content = ''
    #content += geraPCCompleto(filenameContabil, filenameFinanceiro)
    #WriteFile("PovoamentoCompleto.sql", content)
    
    filename = 'LancamentosCC.csv'
    content = ''
    content += geraLancamento(filename)
    print (content)
    
    