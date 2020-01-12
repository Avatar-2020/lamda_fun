import json
import boto3
import botocore.exceptions
import hmac
import hashlib
import base64

USER_POOL_ID='' 
USER_CLIENT_ID=''
CLIENT_SECRET=''


def get_secret_hash(username):
    msg=username+USER_CLIENT_ID
    #particular message which is unique for every user 
    dig=hmac.new(str(CLIENT_SECRET).encode('utf-8'))
    #used by base 64
    msg=str(msg).encode('utf-8')
    #encode our message
    hash_code=hashlib.sha256(msg).hexdigest()
    #hash_code is the hash code which then use by base 64 module
    d2=base64.b64decode(dig).encode()
    return d2

def lambda_handler(event, context):
    # TODO implement
    client=boto3.client('cognito-idp')
    try:
        username = event['username']
        password = event['password']
        code = event['code']        response = client.confirm_sign_up(
        ClientId=CLIENT_ID,
        SecretHash=get_secret_hash(username),
        Username=username,
        ConfirmationCode=code,
        ForceAliasCreation=False,       )
    except client.exceptions.UserNotFoundException:
        #return {"error": True, "success": False, "message": "Username doesnt exists"}
        return event    except client.exceptions.CodeMismatchException:
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
