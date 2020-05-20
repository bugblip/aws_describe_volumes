import describe_volumes as dv


if __name__ == '__main__':
    region="us-east-1"
    allvolumeIds = dv.collectVolumeID(region)

    for vid in allvolumeIds:
        volumeDict = dv.describeSingleVolume(region, vid)
        print(volumeDict)
        exit()