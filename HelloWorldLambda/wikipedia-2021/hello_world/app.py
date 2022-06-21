import json
import wikipedia

# prints when function loads
print('Loading function')


def lambda_handler(event, context):
    print(f"event: {event}")
    
    if 'body' in event:
        event = json.loads(event["body"])
    print(f"event body: {event}")
    ## TO DO: Get the wikipedia "entity" from the body of the request
    entity = event["entity"]
    res = wikipedia.summary(entity, sentences=1) # first sentence, result

    # print statements
    print(f"context: {context}, event: {event}")
    print(f"Response from wikipedia API: {res}")
    
    ## TO DO: Format the response as JSON and return the result
    response = {
        "statusCode": "200", 
        "headers": { "Content-type": "application/json" },
        "body": json.dumps({"message": res})
    }
    
    return response
