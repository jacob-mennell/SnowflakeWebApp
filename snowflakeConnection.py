#import relevant libs
from snowflake import connector
import os

#define env variables
password = os.getenv('password')
username = os.getenv('username')

def sfconnect():
    cnx = connector.connect(
        account='ia83659.europe-west2.gcp',
        user=username,
        password=password,
        warehouse='COMPUTE_WH',
        database='DEMO_DB',
        schema='PUBLIC',
        role='SYSADMIN')

    return cnx

 