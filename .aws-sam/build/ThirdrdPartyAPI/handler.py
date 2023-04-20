import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ["TABLE_NAME"])

def handler(event, context):
    #print(json.dumps(event))

    table.put_item(
        Item={
            'id': event['detail']['user_id'],
            'req': event['detail']
       }
    )
    
    return {}