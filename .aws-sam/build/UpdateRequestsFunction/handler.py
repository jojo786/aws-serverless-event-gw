import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ["TABLE_NAME"])

client = boto3.client('events')

def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))

    id = event['pathParameters']['id']
    appstatus = event['queryStringParameters']

    ddb = table.update_item(
        Key={
             'id': id
       },
        UpdateExpression="set reqstatus = :reqstatus",
        ExpressionAttributeValues={
            ':reqstatus': reqstatus
        },
    )
    print(ddb)

    eb = client.put_events(
        Entries=[
            {
                'Source': 'com.marketplace.3rdparty1',
                'DetailType': 'marketplace status update',
                "Detail": "{ \"user_id\": \"23545345435\", \"3rdparty\": \"3rdparty1\", \"option1\": \"art\", \"option2\": \"cs\", \"status\": \"accepted\"}",
                'EventBusName': 'marketplace',
            },
        ],
    )
    print(eb)
    
    return {
        'statusCode': 200
    }