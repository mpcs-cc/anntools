################################################################################
#   Nov 17, 2011
#   Authors: Vlad Makarov, Chris Yoon
#   Language: Python
#   OS: UNIX/Linux, MAC OSX
#   Copyright (c) 2011, The Mount Sinai School of Medicine

#   Available under BSD  licence

#   Redistribution and use in source and binary forms, with or without modification,
#   are permitted provided that the following conditions are met:
#
#   Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation and/or
#   other materials provided with the distribution.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#   ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#   WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
#   IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
#   INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#   BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
#   OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#   NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
#   EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
################################################################################

import os
import json
import pymysql
import boto3
from botocore.exceptions import ClientError

AWS_REGION_NAME = os.environ['AWS_REGION_NAME'] if ('AWS_REGION_NAME' in  os.environ) else "us-east-1"

# Get RDS secret from AWS Secrets Manager
asm = boto3.client('secretsmanager', region_name=AWS_REGION_NAME)
try:
    asm_response = asm.get_secret_value(SecretId='ads/anntools_database')
    rds_secret = json.loads(asm_response['SecretString'])
except ClientError as e:
    print(f"Unable to retrieve RDS credentials from AWS Secrets Manager: {e}")
    raise e

# Extract database connection parameters
rds_host = rds_secret['host']
mysql_port = rds_secret['port']
username = rds_secret['username']
password = rds_secret['password']
database_name = 'annotator'


def conn2annotator():
    # Return a connection to the database
    return pymysql.connect(
        host=rds_host,
        port=mysql_port,
        user=username,
        passwd=password,
        db=database_name)

### EOF