import boto3
from botocore.exceptions import ClientError
from typing import NamedTuple


class CognitoConfig(NamedTuple):
    region: str = "ap-southeast-1"
    user_pool_id: str = "ap-southeast-1_FG9cOimAA"


class CognitoUser:

    def authenticate(self, username=None, password=None):
        pass

    def login(self):
        pass

    def register(self):
        pass

    def get_user(self, access_token):
        client = boto3.client('cognito-idp', region_name=CognitoConfig.region)
        try:
            response = client.get_user(AccessToken=access_token.replace('Bearer ', ''))
        except ClientError:
            print("AWS Client Error")

        return response
