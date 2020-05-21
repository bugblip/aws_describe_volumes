import boto3
import datetime
import sys

def collectVolumeID(region):
    client = boto3.client('ec2',region_name=region)
    allvolumeIds = []
    response = client.describe_volumes()
    volData=response['Volumes']
    volCount= len(volData)
    if (volCount > 0):
        print(f"There are {volCount} volumes in {region}")
    else:
        print(f"No EBS volume found in {region}")
        sys.exit()
    for vc in range (0, len(volData)):
        id = volData[vc]['VolumeId']
        allvolumeIds.append(id)
    return allvolumeIds
    
def describeSingleVolume(region, vid):
    client = boto3.client('ec2',region_name=region)
    volumeDict = {}
    response = client.describe_volumes(VolumeIds=[vid])
    volData=response['Volumes'][0]
    #print(volData)
    
    #DataCollection & Adding Data to data dictionary

    volumeDict["VolumeId"]          = volData.get("VolumeId","-")
    volumeDict["Size"]              = volData.get("Size","-")
    volumeDict["VolumeType"]        = volData.get("VolumeType","-")
    volumeDict["Iops"]              = volData.get("Iops","-")
    volumeDict["State"]             = volData.get("State","-")
    volumeDict['AvailabilityZone']  = volData.get("AvailabilityZone","-")
    volumeDict['Encrypted']         = volData.get("Encrypted","-")
    volumeDict["KmsKeyId"]          = volData.get("KmsKeyId","-")
    volumeDict["SnapshotId"]        = volData.get("SnapshotId","-")
    volumeDict["MultiAttach"]       = volData.get("MultiAttachEnabled","-")
    volumeDict["LaunchTime"]        = str(volData.get("CreateTime","-"))

    return volumeDict