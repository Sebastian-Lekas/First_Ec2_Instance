import json 

def handler(event, context):
    print('request: {}'.format(json.dumps(events)))
    return {
        'statusCode': 200,
        'headers':{
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, {}! You have a hit \n'.format(event['queryStringParameters']['name'])
    }
