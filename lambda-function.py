import json
import boto3
import os
import time

cloudfront = boto3.client('cloudfront')

def lambda_handler(event, context):
    distribution_id = os.environ.get('DISTRIBUTION_ID')

    # Check if the Distribution ID is provided
    if not distribution_id:
        return {
            'statusCode': 400,
            'body': json.dumps('Environment variable DISTRIBUTION_ID is missing')
        }

    try:
        response = cloudfront.create_invalidation(
            DistributionId=distribution_id,
            InvalidationBatch={
                'Paths': {
                    'Quantity': 1, # Number of paths to invalidate
                    'Items': ['/*'] # List of paths to invalidate (/* means all files)
                },
                'CallerReference': f'invalidation-{int(time.time())}'
            }
        )

        # Return a success response
        return {
            'statusCode': 200,
            'body': json.dumps('Invalidation successful')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error creating invalidation: {str(e)}')
        }
