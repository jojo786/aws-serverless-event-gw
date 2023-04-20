import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("marketplace-requests-23TVXBFDBL6T")

def handler(event, context):
    #print(json.dumps(event))

    table.put_item(
        Item={
            'id': event['detail']['user_id'],
            'req': event['detail']
       }
    )
    
    return {}