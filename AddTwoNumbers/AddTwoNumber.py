def lambda_handler(event, context):
    """
    Lambda function to add two numbers.

    Expected input event structure:
    {
        "number1": <number>,
        "number2": <number>
    }
    """
    # Retrieve the two numbers, defaulting to 0 if not provided.
    number1 = event.get("number1", 0)
    number2 = event.get("number2", 0)

    # Calculate the sum
    result = number1 + number2

    # Return the result
    return {
        "statusCode": 200,
        "body": {
            "result": result
        }
    }



"""
How to Test This Function:
Create a new test event in the Lambda console with a JSON body like
{
    "number1": 10,
    "number2": 15
}
Save your event to a file and then run

aws lambda invoke --function-name YourLambdaFunctionName --payload file://event.json response.json

"""
