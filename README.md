# serverless-sar-lambda-layer-test

Example applying a lambda layer from a Serverless Application Registry App to a function in a Serverless Framework template.

Attempting to implement as suggested by Jeremy Daly in [off-by-none](https://www.jeremydaly.com/newsletter-issue-52/) following examples from https://serverless.pub/sar-layers/ and https://medium.com/theburningmonk-com/how-to-include-serverless-repository-apps-in-serverless-yml-6d8233c5d684
 
The SAR application simply creates a lambda layer with the python requests library installed. 
https://github.com/aaronosb/requests-lambda-layer-python-SAR

The lambda function itself is pretty simple but can be used to verify the requests lib dependency was installed in the runtime
```python
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
```

## HELP NEEDED

```
  Serverless Error ---------------------------------------
 
  An error occurred: sar-layer-example-stack-dev - Template error: resource RequirementsLayerApp does not support attribute type Outputs in Fn::GetAtt.
```

#### Serverless Template
```yaml
service: 
  name: sar-layer-example-stack
provider:
  name: aws
  runtime: python3.7
  stage: dev
  timeout: 30
  region: us-east-1
functions:
  hello:
    handler: code/hello.lambda_handler
    layers:
      - !GetAtt RequirementsLayerApp.Outputs.LayerVersion
    events:
    - http:
        path: /
        method: get
resources:
  Transform: AWS::Serverless-2016-10-31
  Resources:
    RequirementsLayerApp:
      Type: AWS::Serverless::Application
      Properties:
        Location:
          ApplicationId: arn:aws:serverlessrepo:us-east-1:721343429908:applications/requests-python-layer-app
          SemanticVersion: 1.0.0
```

It looks like the reference to `- !GetAtt RequirementsLayerApp.Outputs.LayerVersion` the outputs of the SAR App are not able to be referenced as part of the serverless framework template.

### Looking for suggestions on how to access the lambda layer arn that is part of the SAR App? 