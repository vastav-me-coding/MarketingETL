// config/develop.tfvars
environment         = "production"
app_name = "affinity-tds"
account_id          = "377633137458"
private_subnet_1_name = "AWS-Affinity-US-Prode1-PrivateSubnet1"
private_subnet_0_name = "AWS-Affinity-US-Prode1-PrivateSubnet0"
security_group_web_name = "AWS-Affinity-US-Prode1-AON-WEB-ACCESS"
security_group_app_common_name = "AWS-Affinity-US-Prode1-COMMON-APP-ACCESS"
security_group_db_common_name = "AWS-Affinity-US-Prode1-COMMON-DB-ACCESS"
security_group_db_name = "AWS-Affinity-US-Prode1-AON-DB-ACCESS"
vpc_id              = "vpc-0411cd07123d2ba4d"
region              = "us-east-1"
appid = "AR4262-PR001"

kms_key_id = "b9aebd01-9adb-4288-a192-759ea191b693"
lambda_name = "ods-etl-hc-mkt-notebook"
image_uri = "948273211232.dkr.ecr.us-east-1.amazonaws.com/affinity-ods-ar4262-pr001-ods-etl-hc-mkt-notebook:latest"
sfmc_api_credentials_secret_arn = "arn:aws:secretsmanager:us-east-1:377633137458:secret:affinity-ods-ar4262-dv001-sfmc-api-credentials-ui4ykt"
rds_credentials_secret_arn = "arn:aws:secretsmanager:us-east-1:377633137458:secret:rds-master-credentials-secret-affinity-ods2-Uak2gc"
rds_prod_credentials_secret_arn = "arn:aws:secretsmanager:us-east-1:377633137458:secret:rds-master-credentials-secret-affinity-awb2-N3mWJY"
rds_cluster_endpoint = "affinity-ods2.cluster-cyfwyevzbce3.us-east-1.rds.amazonaws.com"
lambda_execution_role_name = "affinity-tds-ar4262-pr001-s3-sqs-lambda-role"
lambda_execution_role_arn = "arn:aws:iam::377633137458:role/app/affinity-tds-ar4262-pr001-sqs-lambda-role"
s3_bucket = "affinity-artifacts-prod-us-east-1"
token_url = "https://mcbz9h5rpbkc5z8pc4v6tkfbwzh8.auth.marketingcloudapis.com/v2/token"

sfmc_url = "https://mcbz9h5rpbkc5z8pc4v6tkfbwzh8.rest.marketingcloudapis.com/data/v1/async/dataextensions/key:492F919E-5363-40D9-91F3-E4BD3DB8BBF2/rows"

deployments = {
    ods_aws_lambda_apis_multiple = {
        blue = {
            enabled = true
            overrides = {
                appid = "AR4262-PR001"
                create_s3_sqs_lambda_role = true
            }
        }
        green = {
            enabled = false
            overrides = {
                appid = "AR4262-PR002"
            }
        }
    }
}