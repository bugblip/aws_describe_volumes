import boto3
import datetime

def collectVolumeID(region):
    client = boto3.client('ec2',region_name=region)
    allvolumeIds = []
    response = client.describe_volumes()
    volData=response['Volumes']
    for vc in range (0, len(volData)):
        id = volData[vc]['VolumeId']
        allvolumeIds.append(id)
    return allvolumeIds
    
def describeSingleVolume(region, vid):
    client = boto3.client('ec2',region_name=region)
    volumeDict = {}
    response = client.describe_volumes(VolumeIds=[vid])
    volData=response['Volumes'][0]
    
    #DataCollection & Adding Data to data dictionary

    volumeDict['AvailabilityZone']  = volData.get("AvailabilityZone","-")
    volumeDict['Encrypted']         = volData.get("Encrypted","-")
    volumeDict["Size"]              = volData.get("Size","-")
    volumeDict["State"]             = volData.get("State","-")
    volumeDict["VolumeId"]          = volData.get("VolumeId","-")
    volumeDict["Iops"]              = volData.get("Iops","-")
    volumeDict["VolumeType"]        = volData.get("VolumeType","-")
    volumeDict["MultiAttach"]       = volData.get("MultiAttachEnabled","-")
    volumeDict["LaunchTime"]        = str(volData.get("CreateTime","-"))

    return volumeDict