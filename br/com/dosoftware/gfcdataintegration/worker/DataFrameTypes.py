# coding=utf-8
import pandas
from br.com.dosoftware.gfcdataintegration.util.Constantes import Constantes

def specifyDataFramePlanoContas():
    columns = ['DT_ALT', 'COD_NAT', 'IND_CTA', 'NIVEL', 'COD_CTA', 'COD_CTA_SUP', 'CTA', 'IND_DC']
    type = [Constantes.TYPE_DATE, Constantes.TYPE_STR, Constantes.TYPE_STR, Constantes.TYPE_STR, Constantes.TYPE_STR, Constantes.TYPE_STR, Constantes.TYPE_STR, Constantes.TYPE_STR]
    dict_types = dict(zip(columns, type))
    df = pandas.DataFrame(columns=columns, dtype=str)
    return df, dict_types

def specifyDataFrameCaixaBanco():
    columns = ['IDPLANOCONTAS'] 
    type = [Constantes.TYPE_QUERY]
    dict_types = dict(zip(columns, type))
    df = pandas.DataFrame(columns=columns, dtype=str)
    return df, dict_types

def specifyDataFrameSaldoConta():
    columns = ['IDPLANOCONTAS', 'IDCENTROCUSTO', 'DT_SALDO', 'VL_SALDO']
    type = [Constantes.TYPE_QUERY, Constantes.TYPE_QUERY, Constantes.TYPE_DATE, Constantes.TYPE_MONEY]
    dict_types = dict(zip(columns, type))
    df = pandas.DataFrame(columns=columns, dtype=str)
    df[['VL_SALDO']] = df[['VL_SALDO']].astype(float)
    return df, dict_types

def specifyDataFramePlanoContasFinanceiro():
    columns = ['IDPLANOCONTAS', 'IND_CTA', 'NIVEL', 'COD_CTA', 'COD_CTA_SUP', 'CTA', 'TIPO']
    type = [Constantes.TYPE_QUERY, Constantes.TYPE_STR, Constantes.TYPE_STR, Constantes.TYPE_STR, Constantes.TYPE_STR, Constantes.TYPE_STR, Constantes.TYPE_STR, Constantes.TYPE_STR]
    dict_types = dict(zip(columns, type))
    df = pandas.DataFrame(columns=columns, dtype=str)
    return df, dict_types


    
