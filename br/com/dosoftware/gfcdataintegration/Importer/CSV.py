# coding=utf-8
import os
import pandas
import csv
import codecs

from br.com.dosoftware.gfcdataintegration.util.Constantes import Constantes
from pandas.core.frame import DataFrame
path = 'C:\\Users\\Angelin\\workspace\\GFCDataIntegration'


def readCSV(filename, delimiter=Constantes.delimiter):
    filename = (os.path.join(path, 'resources', 'CSV', 'CC', filename))
    with codecs.open(filename, 'r', encoding='utf-8') as csvfile:
        freader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
        
        for row in freader:
            data = ', '.join(row)
            print (data)

def readCSV2PandasDF(filename, delimiter=Constantes.delimiter):
    filename = (os.path.join(path, 'resources', 'CSV', 'CC', filename))
    data = pandas.read_csv(filename, delimiter=delimiter, encoding='cp1252', dtype=str)
    return data

def convertPandasDF2Matrix(df): # returning a numpy (nd)array
    ndArray = df.as_matrix()
    ndArray = ndArray.T # transpose, other matrix operations also supports
    return ndArray

def splitFile(path, number_lines):
	with open(path) as f:
		content = f.readlines();
	
	splited = content
	max_lines = len(splited)
	listFiles = []
	actualFile = []
	for i in splited:
		if len(actualFile) > number_lines:
			listFiles += [actualFile]
			actualFile = []
		actualFile += [i]

		
	count = 1
	out = ""
	for i in listFiles:
		out = "\n".join(i)

		filebyPoint = path.split(".")
		if (len(filebyPoint) == 2):
			outputFile = filebyPoint[0]+"_Part"+str(count)+"."+filebyPoint[1]
		else:
			outputFile = path+str(count)
		
		with open(outputFile,'w') as f:
			print(outputFile)
			f.write(out)
			f.close()

		out = ""
		count+=1


def WriteFile(filename, content):
    filename = (os.path.join(path, 'resources', 'CSV', 'CC', filename))
    file = open(filename, "w")
    file.write(content)
    file.close()
    
