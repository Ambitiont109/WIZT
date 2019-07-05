import random
import string
import boto3
#conf for boto3 for AWS
# Yuo need to have AWS credentails in ~/.aws/credentials
# [default]
# aws_access_key_id=AKIAWCM52PJVRQEZ6744
# aws_secret_access_key=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
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def upload_file(file):
    s3 = boto3.resource('s3')
    s3_bucket_name = 'pit'
    s3.Bucket(s3_bucket_name).put_object(Key='test',Body=file)
    bucket_location = boto3.client('s3').get_bucket_location(Bucket=s3_bucket_name)
    object_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
        bucket_location['LocationConstraint'],
        s3_bucket_name,
        key_name)


def send_push_notification(target_arn, subject, message):
    client = boto3.client('sns', region_name='ap-southeast-1')
    # target_arn = "arn:aws:sns:ap-southeast-1:417479686763:endpoint/GCM/wizt-new/1a298313-61dd-3e04-9b33-99f0cfa90210"
    response = client.publish(
        TargetArn=target_arn,  # Target Amazon Resource Name
        Message=message,
        Subject=subject,
        MessageStructure='string'
    )


def send_broadcast_notification(topic_arn, subject, message):
    client = boto3.client('sns', region_name='ap-southeast-1')
    # target_arn = "arn:aws:sns:ap-southeast-1:417479686763:endpoint/GCM/wizt-new/1a298313-61dd-3e04-9b33-99f0cfa90210"
    response = client.publish(
        TopicArn=topic_arn,  # Target Amazon Resource Name
        Message=message,
        Subject=subject,
        MessageStructure='string'
    )