# coding=utf-8
import numpy
import pandas
from br.com.dosoftware.gfcdataintegration.util import getCOD_CTA_SUP, applyMask, applyNivel
from br.com.dosoftware.gfcdataintegration.util.Constantes import Constantes

def specifyDataFramePlanoContas():
    columns = ['DT_ALT', 'COD_NAT', 'IND_CTA', 'NIVEL', 'COD_CTA', 'COD_CTA_SUP', 'CTA', 'IND_DC']
    return pandas.DataFrame(columns=columns, dtype=str)

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
    #ind_dc = str(ind_dc)
    #if (ind_dc.find('Credora') != -1):
    #    return 'C'
    #if (ind_dc.find('Devedora') != -1):
    #    return 'D'

def createPlanoContasDataFrame (dtCSV, dtPlanoContas):
    mask = Constantes.mask
    dtPlanoContas['COD_NAT'] = [convertCOD_NAT(x) for x in dtCSV['COD_NAT']]
    dtPlanoContas['IND_CTA'] = [convertIND_CTA(x) for x in dtCSV['IND_CTA']]
    dtPlanoContas['NIVEL'] = [applyNivel(applyMask(x, mask)) for x in dtCSV['COD_CTA']]
    dtPlanoContas['COD_CTA'] = [applyMask(x, mask) for x in dtCSV['COD_CTA']]
    dtPlanoContas['COD_CTA_SUP'] = [getCOD_CTA_SUP(applyMask(x, mask)) for x in dtCSV['COD_CTA']]
    dtPlanoContas['CTA'] = dtCSV['CTA']
    dtPlanoContas['IND_DC'] = [convertIND_DC(x) for x in dtCSV['IND_DC']]
    return dtPlanoContas
    
