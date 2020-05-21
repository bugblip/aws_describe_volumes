import describe_volumes as dv
import csv_reader_writer as crw
import sys
import datetime

def runtime(startTime):
    endTime = datetime.datetime.now()
    executionTime = endTime - startTime
    print (f"Script RunTime = {executionTime}".center(80,"-"))

if __name__ == '__main__':
    
    startTime = datetime.datetime.now()
    print (f"Execution started at = {startTime}".center(80,"-"))
    regions = ["us-east-2","us-east-1","us-west-1","us-west-2","af-south-1","ap-east-1","ap-south-1","ap-northeast-3","ap-northeast-2","ap-southeast-1","ap-southeast-2","ap-northeast-1","ca-central-1","eu-central-1","eu-west-1","eu-west-2","eu-south-1","eu-west-3","eu-north-1","me-south-1","sa-east-1"]
    
    print("Select the region in which the AWS resource exist")
    for r in range(0, len(regions)):
        print(f"{r+1}.\t{regions[r]}")
        
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
