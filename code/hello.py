import requests

def lambda_handler(event, context):
    try:
        response = requests.get('https://api.github.com')
        return {
            'statusCode': '200',
            'body': response.text,
        }      
    except Exception as e:
        print(e)
        return {
        'statusCode': '500',
        }     

