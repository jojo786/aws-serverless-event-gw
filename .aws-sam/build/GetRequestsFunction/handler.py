import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ["TABLE_NAME"])

def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    #print(json.dumps(event))

    id = event['pathParameters']['id']
    response = table.get_item(Key={'id': id})
    
    #print(response)
    return {
        'statusCode': 200,
        'body':  json.dumps(response['Item']['req'])
        }