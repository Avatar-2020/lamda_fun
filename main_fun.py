import json
import boto3
import base64
import datetime

exact_date=datetime.datetime.now()
parent=boto3.client('cognito-idp')
exact_date=exact_date.strftime('%x')

dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table('Accident_Case')
s3=boto3.client('s3')
invoke_lambda=boto3.client('lambda')



def list_fun(long,lat):
    partnerlist=[]
    return partnerlist
 
def lambda_handler(event, context):
    # TODO implement
    
    latitude=event['loc']['lat']
    longitude=event['loc']['long']
    device_id=event['deviceId']
    AUID=device_id+longitude+latitude+exact_date
    image_64_encode=event['image']
    video_64_encode=event['video']
    image_64_encode=str.encode(image_64_encode)
    video_64_encode=str.encode(video_64_encode)
    
    image_64_decode=base64.encodestring(image_64_encode)
    video_64_decode=base64.encodestring(video_64_encode)
    
    with open("/tmp/log.png","wb") as f:
        f.write(image_64_decode)
    s3.upload_file("/tmp/log.png","bucket2.sih","{}.png".format(AUID))
    
    with open("/tmp/log.mp4","wb") as f:
        f.write(video_64_decode)
    s3.upload_file("/tmp/log.mp4","bucket2.sih","{}.mp4".format(AUID))
    
    #enter info in dynamo db table
    
    table.put_item(Item=json.dumps({'id':AUID,'lat':latitude,'long':longitude,'googleAdd':'https://www.google.com/maps/place/{},{}'.format(latitude,longitude)}))
    
    #payload={"message":"hi you have been invoked ."}
    #resp=invoke_lambda.invoke(FunctionName='lambdafun_2',InvocationType='Event',Payload=json.dumps(payload))
    
    
    partnerlist=list_fun(longitude,latitude)[:]
    response = client.admin_get_user(
    UserPoolId='string',
    Username='string')
    
    #sending push notification to the partnerlist
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
