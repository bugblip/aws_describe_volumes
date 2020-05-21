import describe_volumes as dv
import csv_reader_writer as crw
import sys
import datetime
import boto3


def runtime(startTime):
    endTime = datetime.datetime.now()
    executionTime = endTime - startTime
    print (f"Script RunTime (HH:MM:SS)= {executionTime}".center(100,"-"))
    print("\n")

if __name__ == '__main__':
    
    startTime = datetime.datetime.now()
    print("\n")
    print (f"Execution started at = {startTime}".center(100,"-"))
    
    #Getting AWS Region Names
    regions = []
    client = boto3.client('ec2')
    response = client.describe_regions()
    regData = response['Regions']
    print("Select the region in which the AWS resource exist")
    for i in range (0, len(regData)):
        rid = regData[i].get("RegionName")
        regions.append(rid)
        print(f"{i+1}.\t{rid}")
    
    choice1 = int(input())
    if(choice1 >=1 and choice1 <= len(regions)):
        region = regions[choice1-1]
    else:
        print("Wrong Input, please try again.")
        runtime(startTime)
        sys.exit()
        
    
    #Choices    
    print ("Enter Your choice")
    print(f"1. Details of all EBS volumes in {region}")
    print(f"2. Details of specific EBS volumes in {region} from an input CSV file, containg volumeID(s)")
    choice2 = int(input())
    if (choice2 == 1 ) :
        allvolumeIds = dv.collectVolumeID(region)
        for index,vid in enumerate(allvolumeIds):
            volumeDict = dv.describeSingleVolume(region, vid)
            #Printing the vlue in the CSV file
            crw.csv_writer(index, volumeDict)
    elif (choice2 == 2 ) :
        print(f"Please Enter the complete or absolute path of the input CSV file, containg volumeID(s) of volume(s) in {region}")
        inputfilepath = str(input())
        crw.csv_reader(region, inputfilepath)
    else:
        print("Wrong Input, please try again.")
        runtime(startTime)
        sys.exit()
    
    #calculating script runtime
    runtime(startTime)
