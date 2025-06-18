import json              # To handle JSON request and response bodies
import boto3             # AWS SDK for Python to interact with DynamoDB
import uuid              # For generating unique IDs for each item
import os                # To access environment variables (like table name)
import logging

# Logging setup
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logging.basicConfig(
    format="%(asctime)s : %(name)s : %(levelname)s : %(message)s",
    level=logging.DEBUG,
)

# Ensure region is set (especially for local SAM)
AWS_REGION = os.environ.get('AWS_REGION', 'ap-south-1')
TABLE_NAME = os.environ.get('TABLE_NAME')

# Log to confirm environment setup
logging.info(f"TABLE NAME: {TABLE_NAME}")
logging.info(f"AWS REGION: {AWS_REGION}")

# Initialize DynamoDB resource and get the table reference using env variable
dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
table = dynamodb.Table(TABLE_NAME)


# Main Lambda entry point
def lambda_handler(event, context):
    http_method = event['httpMethod']  # Get HTTP method (GET, POST, etc.)

    # Route based on HTTP method
    if http_method == 'GET':
        return get_items()
    elif http_method == 'POST':
        return create_item(json.loads(event['body']))
    elif http_method == 'PUT':
        item_id = event['pathParameters']['id']
        return update_item(item_id, json.loads(event['body']))
    elif http_method == 'DELETE':
        item_id = event['pathParameters']['id']
        return delete_item(item_id)
    else:
        return response({"message": "Method not allowed"}, 405)

# Retrieve all items from the table
def get_items():
    items = table.scan().get('Items', [])  # Scan the entire table
    logger.info(f"Fetched items: {items}")
    return response(items)

# Add a new item to the table
def create_item(data):
    item = {
        'id': str(uuid.uuid4()),             # Generate a unique ID
        'name': data.get('name'),            # Get 'name' from input JSON
        'description': data.get('description')  # Get 'description' from input JSON
    }
    table.put_item(Item=item)               # Save the item in DynamoDB
    return response(item)

# Update an existing item by ID
def update_item(item_id, data):
    table.update_item(
        Key={'id': item_id},                            # Match item by ID
        UpdateExpression="set #n=:n, description=:d",   # Update name and description
        ExpressionAttributeNames={'#n': 'name'},        # 'name' is a reserved keyword
        ExpressionAttributeValues={':n': data['name'], ':d': data['description']}
    )
    return response({"message": "Updated successfully"})

# Delete item by ID
def delete_item(item_id):
    table.delete_item(Key={'id': item_id})
    return response({"message": "Deleted successfully"})

# Helper function to return JSON response
def response(body, status=200):
    return {
        "statusCode": status,
        "body": json.dumps(body),                       # Convert body to JSON string
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"          # Allow frontend apps to call API (CORS)
        }
    }

# Create -
#curl -X POST https://abcd1234.execute-api.ap-south-1.amazonaws.com/Prod/items \
# -H "Content-Type: application/json" \
#-d '{"name": "Notebook", "description": "A ruled notebook with 100 pages"}'

# Get -
# https://a1pgm4ggq0.execute-api.ap-south-1.amazonaws.com/Prod/items

# Delete -
# curl -X DELETE https://abcd1234.execute-api.ap-south-1.amazonaws.com/Prod/items/d39f3f72-abc3-4cb2-b5e6-b28e1fc8a300


# Update -
# curl -X PUT https://a1pgm4ggq0.execute-api.ap-south-1.amazonaws.com/Prod/items/4f0df8e7-b4e8-4e77-a47d-92e93b37dd3e 
# -H "Content-Type: application/json" -d '{"name": "Updated Item Name", "description": "Updated description"}'


# test case in labda :-
#POST
#{
 # "httpMethod": "POST",
  #"body": "{\"name\": \"Book\", \"description\": \"A mystery novel\"}"
#}

#Delete
#{
 # "httpMethod": "DELETE",
  #"pathParameters": {
 #   "id": "PASTE-YOUR-ITEM-ID-HERE"
 # }
#}

# get
#{
 # "httpMethod": "GET"
#}

# POST
# {
  # "httpMethod": "PUT",
  # "pathParameters": {
  #   "id": "PASTE-YOUR-ITEM-ID-HERE"
 #  },
 #  "body": "{\"name\": \"Updated Name\", \"description\": \"Updated description\"}"
# }