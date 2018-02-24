import logging
import boto3
from boto3.session import Session

print('Loading function... ')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# set your access key here!!
AWS_ACCESS_KEY = 'AKIAJTR62TDCMHIFOH3A'
# set your secret access key here!!
AWS_ACCESS_SECRET = '9Z/jzM0C+haty7f2hwroK9ADmw06wq/EcnMgrcEj'

# option
AWS_REGION = 'ap-northeast-1'
EC2_TARGET_NAME_TAG = 'StopTargetInstance'

def handler(event, context):
    
    session = Session(aws_access_key_id=AWS_ACCESS_KEY,
                      aws_secret_access_key=AWS_ACCESS_SECRET,
                      region_name=AWS_REGION)
    ec2 = session.client('ec2')
    filters = [{'Name' :'tag:Name', 'Values':[ EC2_TARGET_NAME_TAG ] }]
    describes = ec2.describe_instances(Filters=filters)
    #debug
    #logging.info(describes)
    instances_id = []
    for describe in describes['Reservations']:
        instances_id.append(describe['Instances'][0]['InstanceId'])
    if len(instances_id)>0:
        logging.info('stop instances')
        ec2.stop_instances(InstanceIds=instances_id)
    else:
        logging.info('no target instance')

    return 'done!!!'
