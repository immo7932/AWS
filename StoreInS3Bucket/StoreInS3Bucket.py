import boto3
import base64

# Initialize the S3 client outside of the handler to improve performance with container reuse.
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    """
    Lambda function to store a document or PDF file in an S3 bucket.

    Expected event structure:
    {
        "bucket": "<your-s3-bucket-name>",
        "key": "<desired-object-key.pdf>",
        "file_content": "<base64-encoded-content>"
    }
    """
    # Get parameters from the event
    bucket_name = event.get('bucket')
    key = event.get('key')
    file_content_base64 = event.get('file_content')

    # Validate parameters
    if not bucket_name or not key or not file_content_base64:
        return {
            "statusCode": 400,
            "body": "Missing required parameters: bucket, key, or file_content."
        }

    try:
        # Decode the base64 encoded content
        file_content = base64.b64decode(file_content_base64)

        # Upload the file to S3
        response = s3_client.put_object(
            Bucket=bucket_name,
            Key=key,
            Body=file_content,
            ContentType="application/pdf"
        )

        return {
            "statusCode": 200,
            "body": "File uploaded successfully.",
            "s3_response": response
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error uploading file: {str(e)}"
        }
