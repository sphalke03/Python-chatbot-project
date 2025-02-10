import boto3

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.create_table(
    TableName="ChatbotConversations",
    KeySchema=[{"AttributeName": "session_id", "KeyType": "HASH"}],
    AttributeDefinitions=[{"AttributeName": "session_id", "AttributeType": "S"}],
    ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
)

print("DynamoDB Table Created:", table.table_status)
