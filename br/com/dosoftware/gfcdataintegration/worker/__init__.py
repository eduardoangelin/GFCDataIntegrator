# coding=utf-8
import numpy
import pandas
from br.com.dosoftware.gfcdataintegration.util import getCOD_CTA_SUP, applyMask, applyNivel
from br.com.dosoftware.gfcdataintegration.util.Constantes import Constantes
from br.com.dosoftware.gfcdataintegration.util.SQLServer import SQLServer


def convertIND_CTA(ind_cta):
    return str(ind_cta[0])
        
def convertCOD_NAT(cod_nat):
    cod_nat = str(cod_nat)
    if (cod_nat.find('Conta de Ativo') != -1):
        return '01'
    if (cod_nat.find('Conta de Passivo') != -1):
        return '02'
    if (cod_nat.find('Patrimônio Líquido') != -1):
        return '03'
    if (cod_nat.find('Conta de Resultado') != -1):
        return '04'

def convertIND_DC(ind_dc):
    return str(ind_dc[0])

def createPlanoContasDataFrame (dtCSV, dtPlanoContas):
    mask = Constantes.mask
    dtPlanoContas['DT_ALT'] = ['2016-01-01' for x in dtCSV['COD_NAT']]
    dtPlanoContas['COD_NAT'] = [convertCOD_NAT(x) for x in dtCSV['COD_NAT']]
    dtPlanoContas['IND_CTA'] = [convertIND_CTA(x) for x in dtCSV['IND_CTA']]
    dtPlanoContas['NIVEL'] = [applyNivel(applyMask(x, mask)) for x in dtCSV['COD_CTA']]
    dtPlanoContas['COD_CTA'] = [applyMask(x, mask) for x in dtCSV['COD_CTA']]
    dtPlanoContas['COD_CTA_SUP'] = [getCOD_CTA_SUP(applyMask(x, mask)) for x in dtCSV['COD_CTA']]
    dtPlanoContas['CTA'] = dtCSV['CTA']
    dtPlanoContas['IND_DC'] = [convertIND_DC(x) for x in dtCSV['IND_DC']]
    return dtPlanoContas

def createCaixaBancoDataFrame (dtCSV, dtCaixaBanco):
    for index, row in dtCSV.iterrows():
        #print row['c1'], row['c2']
        #for cod_cta, tipo_conta, ind_cta in dtCSV['COD_CTA'], dtCSV['TIPO_CONTA'], dtCSV['IND_CTA']:
        cod_cta = applyMask(row['COD_CTA'], Constantes.mask)
        tipo_conta = row['TIPO_CONTA']
        ind_cta = row['IND_CTA']
        if (tipo_conta == Constantes.CX_BCO and ind_cta == Constantes.ANALITICA):
            newIndex = len(dtCaixaBanco)
            dtCaixaBanco.loc[newIndex, 'IDPLANOCONTAS'] = SQLServer().getIDPlanoContasByCodigo(cod_cta)
            
    return dtCaixaBanco

def createSaldoContaDataFrame (dtCSV, dtSaldoConta):
    for index, row in dtCSV.iterrows():
    #for cod_cta, ind_cta in dtCSV['COD_CTA'], dtCSV['IND_CTA']:
        cod_cta = applyMask(row['COD_CTA'], Constantes.mask)
        ind_cta = row['IND_CTA']
        if (ind_cta == Constantes.ANALITICA):
            newIndex = len(dtSaldoConta)
            dtSaldoConta.loc[newIndex, 'IDPLANOCONTAS'] = SQLServer().getIDPlanoContasByCodigo(cod_cta)
            dtSaldoConta.loc[newIndex, 'IDCENTROCUSTO'] = None
            dtSaldoConta.loc[newIndex, 'DT_SALDO'] = Constantes.DATA_ALT
            dtSaldoConta.loc[newIndex, 'VL_SALDO'] = 0
            
    return dtSaldoConta
    
    
