import csv
import numpy as np

def getDataSource(data_path):
    sizeOfTV = []
    averageTime = []
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sizeOfTV.append(float(row["Size of TV"]))
            averageTime.append(float(row["Average time spent watching TV in a week (hours)"]))
    
    return{"x":sizeOfTV,"y":averageTime}

def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("corelationIs: ",corelation[0,1])

def setup():
    data_path = "Size of TV,_Average time spent watching TV in a week (hours).csv"
    dataSource = getDataSource(data_path)
    findCorelation(dataSource)        

setup()    

