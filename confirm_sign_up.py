import json
import boto3
import botocore.exceptions
import hmac
import hashlib
import base64


USER_POOL_ID='us-east-1_f4wfaV3pb' 
CLIENT_ID='3ln8ih6mv4ibpvetelt5cosj1a'
CLIENT_SECRET='lvo3vjoh4hevdcue4gkss25n9bubrsm6eah0reim56uiv2hsosu'


def get_secret_hash(username):
    msg = username + CLIENT_ID
    dig = hmac.new(str(CLIENT_SECRET).encode('utf-8'), 
    msg = str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
    d2 = base64.b64encode(dig).decode()
    return d2




def lambda_handler(event, context):
    
        
    client = boto3.client('cognito-idp')  
    try:
        username = event['username']
        password = event['password']
        code = event['code']        
        response = client.confirm_sign_up(
        ClientId=CLIENT_ID,
        SecretHash=get_secret_hash(username),
        Username=username,
        ConfirmationCode=code,
        ForceAliasCreation=False)
    except client.exceptions.UserNotFoundException:
        #return {"error": True, "success": False, "message": "Username doesnt exists"}
        return event    
    except client.exceptions.CodeMismatchException:
        return {"error": True, "success": False, "message": "Invalid Verification code"}
        
    except client.exceptions.NotAuthorizedException:
        return {"error": True, "success": False, "message": "User is already confirmed"}
    
    except Exception as e:
        return {"error": True, "success": False, "message": f"Unknown error {e.__str__()} "}
      
    return event
    
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
