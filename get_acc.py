
import json
import boto3

dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table('Accident_Case')

def lambda_handler(event,context):
         response = table.get_item(
        Key={
            'id':event['id']
        }
    )


