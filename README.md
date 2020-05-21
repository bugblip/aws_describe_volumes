### Features

This code will generate a CSV output file with details of EBS Volumes in a particular region.

The output file will include the following details.

- VolumeId
- Size
- VolumeType
- Iops
- State
- AvailabilityZone
- Encrypted
- KmsKeyId
- SnapshotId
- MultiAttachEnabled
- LaunchTime

### Usage

Run the main file using `python main.py` . The first input will ask for the AWS region where the EC2 Describe volumes API will be called.

After that, the code will give the user 2 options,
> 1. Details of all EBS volumes in {region}
> 2. Details of specific EBS volumes in {region} from an input CSV file, containg volumeID(s)

- For the 1st option, no extra input is required.
- For the 2nd option, the path of an input CSV file containing volume ids is required. (for ex, /home/ec2-user/environment/temp/samplefile.csv)

The input file will be in following format
```
vol-092b4xxxxxxxxxx
vol-092b4xxxxxxxxxx
vol-092b4xxxxxxxxxx
vol-092b4xxxxxxxxxx
```

The output file will be generated with the following name format `output_ddmmYYYY_HHMMSS` in the present working directory.
