environment = "develop"
account_id = "968921834094"
private_subnet_0_name = "AWS-AFFINITY-US-DEVI1-VDC-PrivateSubnet0"
security_group_web_name = "DEVINT-AON-WEB-ACCESS"
security_group_app_common_name = "DEVINT-COMMON-APP-ACCESS"
security_group_db_common_name = "DEVINT-COMMON-DB-ACCESS"
security_group_db_name = "DEVINT-AON-DB-ACCESS"
vpc_id = "vpc-0ced58fcc9c685c28"
region = "us-east-1"
appid = "AR4262-DV001"

kms_key_id="a7e9e213-4086-48cf-af1e-918e65c5f390"
lambda_name = "ods-etl-hc-mkt-notebook"
image_uri = ""
rds_credentials_secret_arn = "arn:aws:secretsmanager:us-east-1:968921834094:secret:affinity-ods2-ar4262-dv001-rds-master-credentials-169S6S"
rds_prod_credentials_secret_arn = "arn:aws:secretsmanager:us-east-1:968921834094:secret:rds-master-credentials-secret-affinity-awb2-production-ylTHKh"
sfmc_api_credentials_secret_arn = "arn:aws:secretsmanager:us-east-1:968921834094:secret:affinity-ods-ar4262-dv001-sfmc-api-credentials-RbEIMF"
rds_cluster_endpoint = "affinity-ods2-develop.cluster-cj3qp6qspcpk.us-east-1.rds.amazonaws.com"
lambda_execution_role_name = "affinity-tds-ar4262-dv001-s3-sqs-lambda-role"
lambda_execution_role_arn = "arn:aws:iam::968921834094:role/app/affinity-tds-ar4262-dv001-sqs-lambda-role"
s3_bucket = "affinity-ods-ar4262-dv001-app-a360v2"
token_url = "https://mcbz9h5rpbkc5z8pc4v6tkfbwzh8.auth.marketingcloudapis.com/v2/token"

sfmc_url = "https://mcbz9h5rpbkc5z8pc4v6tkfbwzh8.rest.marketingcloudapis.com/data/v1/async/dataextensions/key:492F919E-5363-40D9-91F3-E4BD3DB8BBF2/rows"
deployments = {
     ods_aws_lambda_apis_multiple = {
        "r112" = {
            enabled = true
            overrides = {
                appid = "AR4262-DV001"
            }
        }
    }
}