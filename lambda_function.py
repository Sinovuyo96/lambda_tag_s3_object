####################
# Tag an s3 Object #
####################

import boto3
import json

s3_client = boto3.client('s3')

def lambda_handler(event, context):

    put_tags_response = s3_client.put_object_tagging(
    Bucket='sinovuyo-s3-bucket-2022',
    Key='object/20211102_113907.jpg',    
    Tagging={
        'TagSet': [
            {
                'Key': 'TextBook',
                'Value': 'Research Methods'
                },
         ]
     }
    )
