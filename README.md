

```markdown
# AWS Lambda Function Examples

This repository contains two AWS Lambda function examples to help you get started with common AWS use cases:

1. **Add Two Numbers:**  
   A simple Lambda function that accepts two numbers as input and returns their sum.

2. **Upload Document/PDF to S3:**  
   A Lambda function that accepts a base64-encoded file (such as a document or PDF) and uploads it to a specified S3 bucket.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Function 1: Add Two Numbers](#function-1-add-two-numbers)
  - [Function 2: Upload Document/PDF to S3](#function-2-upload-documentpdf-to-s3)
- [Deployment](#deployment)
- [Permissions](#permissions)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **Add Two Numbers:**  
  A simple Lambda function that adds two numbers provided in the event payload.

- **Upload Document/PDF to S3:**  
  A Lambda function that decodes a base64-encoded file and uploads it to an S3 bucket.

- **Step-by-Step Setup Instructions:**  
  Detailed guidance on how to set up and test each function using the AWS Management Console.

## Requirements

- **AWS Account**  
  Ensure you have an AWS account with the necessary permissions to create Lambda functions and S3 buckets.

- **Python 3.x**  
  The functions in this repository are written in Python.

- **AWS CLI (Optional):**  
  For deploying and testing through the command line.

## Installation

Clone the repository to your local system:

```bash
git clone https://github.com/immo7932/AWS.git
cd AWS
```

This repository contains code examples. Use these examples to create and deploy your Lambda functions as described in the following sections.

## Usage

### Function 1: Add Two Numbers

**Description:**  
This function accepts an event with two numbers and returns their sum.

**Code Example:**

```python
def lambda_handler(event, context):
    """
    AWS Lambda function to add two numbers.

    Expected event structure:
    {
        "number1": <number>,
        "number2": <number>
    }
    """
    number1 = event.get("number1", 0)
    number2 = event.get("number2", 0)
    result = number1 + number2

    return {
        "statusCode": 200,
        "body": {
            "result": result
        }
    }
```

**Testing:**

1. In the AWS Lambda Console, create a new test event with the following JSON payload:

    ```json
    {
        "number1": 10,
        "number2": 15
    }
    ```

2. Run the test, and you should receive a response with the sum, for example:  
   `{"result": 25}`.

---

### Function 2: Upload Document/PDF to S3

**Description:**  
This function uploads a document or PDF file to an S3 bucket. The file must be provided in base64 encoding.

**Code Example:**

```python
import boto3
import base64

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    """
    AWS Lambda function to store a document or PDF file into an S3 bucket.

    Expected event structure:
    {
        "bucket": "<your-s3-bucket-name>",
        "key": "<desired-object-key.pdf>",
        "file_content": "<base64-encoded-content>"
    }
    """
    bucket_name = event.get('bucket')
    key = event.get('key')
    file_content_base64 = event.get('file_content')
    
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
```

**Testing:**

1. In the AWS Lambda Console, create a new test event with a JSON structure like:

    ```json
    {
        "bucket": "your-s3-bucket-name",
        "key": "documents/example.pdf",
        "file_content": "<base64-encoded-string>"
    }
    ```

   > **Tip:** To generate a base64-encoded string for your PDF locally, you can run:
   >
   > ```bash
   > base64 path/to/your/file.pdf > encoded.txt
   > ```
   >
   > Then copy the contents of `encoded.txt` into the `"file_content"` field.

2. Execute the test, and check the function's output to ensure the file is uploaded to your specified S3 bucket.

## Deployment

### Using the AWS Management Console

1. **Log in to the AWS Management Console.**
2. **Navigate to the Lambda Service:**
   - Click on **Services** and select **Lambda**.
3. **Create a New Function:**
   - Click **Create function**.
   - Choose **Author from scratch**.
   - Enter the function name (e.g., `AddTwoNumbers` or `UploadPDFToS3`).
   - Select **Python 3.8** (or your preferred Python runtime).
   - Configure or create an appropriate execution role.
4. **Add the Code:**
   - Paste the corresponding code (from the examples above) into the inline code editor.
   - Click **Deploy**.
5. **Test the Function:**  
   Configure a test event as described under each function's usage section and run the test.

### Using AWS CLI or AWS SAM (Optional)

For automated deployments, consider using AWS CLI or AWS SAM. Refer to the [AWS CLI Documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) and [AWS SAM Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for more details.

## Permissions

- **Add Two Numbers Function:**  
  Uses basic Lambda execution permissions; no additional permissions are required.

- **Upload Document/PDF to S3 Function:**  
  Ensure your Lambda execution role has S3 write permissions. Example IAM policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": "s3:PutObject",
              "Resource": "arn:aws:s3:::your-s3-bucket-name/*"
          }
      ]
  }
  ```

  Replace `your-s3-bucket-name` with your actual S3 bucket name.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or new ideas, please open an issue or submit a pull request. To contribute:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push your changes (`git push origin feature/YourFeature`).
5. Open a pull request detailing your changes.
