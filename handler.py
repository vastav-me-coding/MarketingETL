import os
import logging
import json
import time
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import BIGINT, create_engine, Column, Integer, String, MetaData, DateTime, Float, Text, Date
from sqlalchemy.orm import Session, declarative_base
from secrets_manager import get_secret
from datetime import datetime
import papermill as pm

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# os.environ["RDS_SECRETS_MANAGER_ID"] = "arn:aws:secretsmanager:us-east-1:968921834094:secret:affinity-ods2-ar4262-dv001-rds-master-credentials-169S6S"
# os.environ["AWS_REGION"] = "us-east-1"
# os.environ['RDS_HOST'] = "affinity-ods2-develop.cluster-cj3qp6qspcpk.us-east-1.rds.amazonaws.com"
# os.environ['RDS_DB_NAME'] = "tds"

os.environ['TOKEN_URL'] = "https://mcbz9h5rpbkc5z8pc4v6tkfbwzh8.auth.marketingcloudapis.com/v2/token"
os.environ['SFMC_URL_ACTIVE'] , os.environ['SFMC_URL_LAPSED'] , os.environ['SFMC_URL_QUOTED_NOT_TAKEN'], os.environ['SFMC_URL_ACTIVE_LAPSED']= "https://mcbz9h5rpbkc5z8pc4v6tkfbwzh8.rest.marketingcloudapis.com/data/v1/async/dataextensions/key:492F919E-5363-40D9-91F3-E4BD3DB8BBF2/rows", "https://mcbz9h5rpbkc5z8pc4v6tkfbwzh8.rest.marketingcloudapis.com/data/v1/async/dataextensions/key:F2F7D0C6-B45D-4AC9-86DA-2470EB9181E9/rows", "https://mcbz9h5rpbkc5z8pc4v6tkfbwzh8.rest.marketingcloudapis.com/data/v1/async/dataextensions/key:DC01D033-042F-43B2-9247-4CF625950415/rows", "https://mcbz9h5rpbkc5z8pc4v6tkfbwzh8.rest.marketingcloudapis.com/data/v1/async/dataextensions/key:FFE83A1E-5F6D-4B53-BFBD-F547220697F9/rows"

# Base = declarative_base()
# db_secret = json.loads(get_secret(
#          secret_name=os.environ["RDS_SECRETS_MANAGER_ID"], region_name=os.environ["AWS_REGION"]))
# rds_host = os.environ['RDS_HOST']

# rds_db_name = os.environ['RDS_DB_NAME']
# ods_conn_str = f"mysql+pymysql://{db_secret['username']}:{db_secret['password']}@{rds_host}/{rds_db_name}"

# engine = create_engine(ods_conn_str)
# session = Session(engine)
# meta = MetaData(engine)

# os.environ['NOTEBOOK_OUTPUT_PATH'] = 'C:\\Users\\A0873258\\Downloads\\Temp\\'
# os.environ['S3_BUCKET'] = 'affinity-ods-ar4262-dv001-app-a360v2'


def consume(config=None):
    now = datetime.now()
    start_timestamp = datetime.timestamp(now)
    print(f'Processing Notebook @ {now} | {datetime.timestamp(now)}')
    try:
        print(config)
        global output_file_path
        output_file_path = os.environ.get("NOTEBOOK_OUTPUT_PATH", f"s3://{os.environ['S3_BUCKET']}/jupyter_notebooks_outputs/hc_marketing_etl/") 

        if (config["key"] == "terminated" and config["mode"] == "baseline"):

          notebook = "ods_etl_mkt_hc_lapsed_policies.ipynb"
          baseline(config,notebook,output_file_path) 

        elif (config["key"] == "terminated" and config["mode"] == "incremental"):

          notebook = "ods_etl_mkt_hc_lapsed_policies.ipynb"
          incremental(config,notebook,output_file_path)  

        elif (config["key"] == "pending" and config["mode"] == "baseline"):

          notebook = "ods_etl_mkt_hc_quoted_not_taken_policies.ipynb"
          baseline(config,notebook,output_file_path)

        elif (config["key"] == "pending" and config["mode"] == "incremental"):

          notebook = "ods_etl_mkt_hc_quoted_not_taken_policies.ipynb"
          incremental(config,notebook,output_file_path)

        elif (config["key"] == "active_lapsed" and config["mode"] == "baseline"):

          notebook = "ods_etl_mkt_hc_active_and_lapsed_policies.ipynb"
          baseline(config,notebook,output_file_path) 

        elif (config["key"] == "active_lapsed" and config["mode"] == "incremental"):

          notebook = "ods_etl_mkt_hc_active_and_lapsed_policies.ipynb"
          incremental(config,notebook,output_file_path)    

        elif (config["key"] == " " and config["mode"] == "incremental"):

          notebook = "ods_etl_mkt_hc_active_policies.ipynb"
          incremental(config,notebook,output_file_path)

        else:
          notebook = "ods_etl_mkt_hc_active_policies.ipynb"
          baseline(config,notebook,output_file_path)

        end_timestamp = datetime.timestamp(now)
        print(f'Processed Notebook @ {now} | {datetime.timestamp(now)}')        
        return {'execution_time': end_timestamp - start_timestamp}
    except Exception as e:
        print(e)
        # session.rollback()
        raise e

def baseline(config,notebook,output_file_path):
    key = config['key']
    mode = config['mode']
    output_file_path = output_file_path + f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{notebook}"  
    pm.execute_notebook(notebook, output_file_path, parameters=
        {'limit': config.get('limit',10000),'offset': config.get('offset',0),'key': config.get('key',key),'mode': config.get('mode','baseline')})

def incremental(config,notebook,output_file_path):
    key = config['key']
    mode = config['mode']
    output_file_path = output_file_path + f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{notebook}"     
    pm.execute_notebook(notebook, output_file_path, parameters=
        {'limit': config.get('limit',10000),'offset': config.get('offset',0),'key': config.get('key',key),'mode': config.get('mode','incremental')}) 

# def quoted_not_taken_policies(config):
#     key = config['key']
#     output_file_path_quoted = output_file_path + f"{datetime.now().strftime('%Y%m%d%H%M%S')}_ods_etl_mkt_hc_quoted_not_taken_policies.ipynb"
#     pm.execute_notebook('ods_etl_mkt_hc_quoted_not_taken_policies.ipynb', output_file_path_quoted, parameters=
#         {'limit': config.get('limit',10000),'offset': config.get('offset',0),'key': config.get('key','pending')})   


def handle(event, context):
    start_time = time.time()
    
    # print(engine)
    # print(session)
    if event.get("execution_type", "sqs") == 'scheduled':
      print(consume(config=event))
    else:
      for record in event['Records']:
        payload = record["body"]
        print(consume(config=payload))

    end_time = time.time()

    return {
        "execution_time_sec": end_time - start_time 
    }

# if __name__ == '__main__':
#   handle({"Records": [{"body": {"limit": 10000,"offset": 0,"key": "terminated","mode":"incremental"}}]}, None)
