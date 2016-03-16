# coding=utf-8
import os
import pandas
import csv
import codecs

from br.com.dosoftware.gfcdataintegration.util.Constantes import Constantes
from pandas.core.frame import DataFrame
path = 'C:\\Users\\Angelin\\workspace\\GFCDataIntegration'



def readCSV(filename, delimiter=Constantes.delimiter):
    filename = (os.path.join(path, 'resources', 'CSV', filename))
    with codecs.open(filename, 'r', encoding='utf-8') as csvfile:
        freader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
        
        for row in freader:
            data = ', '.join(row)
            print (data)

def readCSV2PandasDF(filename, delimiter=Constantes.delimiter):
    filename = (os.path.join(path, 'resources', 'CSV', filename))
    data = pandas.read_csv(filename, delimiter=delimiter, encoding='cp1252', dtype=str)
    return data

def convertPandasDF2Matrix(df): # returning a numpy (nd)array
    ndArray = df.as_matrix()
    ndArray = ndArray.T # transpose, other matrix operations also supports
    return ndArray


    