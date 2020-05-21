import boto3
import csv
import os
import datetime

import describe_volumes as dv

#Output File Variables
basename = "output"
suffix = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
filename = "_".join([basename, suffix])
filename = filename+".csv"
cw_path = os.getcwd()
outputFilePath = cw_path +"/"+ filename


def csv_reader(region,inputfilepath):
    try:
        with open(inputfilepath, newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # rowCount = len(list(csv_reader))
            for rowNum, line in enumerate(csv_reader):
                vid=str("".join(line))
                volumeDict = dv.describeSingleVolume(region, vid)
                
                #Writing the data to CSV file
                csv_writer(rowNum, volumeDict)
                
    except Exception as error:
        print(error)
        
def csv_writer(rowNum, volumeDict):
    #Writing to CSV file and formatting       
    with open(filename, 'a') as f:
        if ( rowNum == 0 ):
            print(f"Generating output file at - {outputFilePath}") 
            for key,value in volumeDict.items():
                f.write(f"{key},")
        
        f.write(f"\n")
        for key,value in volumeDict.items():
            f.write(f"{value},")