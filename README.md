# aws-serverless-event-gw
HOW TO INTEGRATE YOUR AWS EVENT-BASED SYSTEM WITH EXTERNAL/LEGACY SYSTEMS USING RESTFUL API

Read the [Blog Post](https://hacksaw.co.za/blog/use-events-internally-and-apis-externally/)

![architecture](Image-ApplicationComposer.jpg)

## How to run it
- Modify the value of `WebhookSiteURL` in [SAM template](https://github.com/jojo786/aws-serverless-event-gw/blob/main/template.yaml) with your chosen API Destination
- [Load template into AWS Application Composer](https://docs.aws.amazon.com/application-composer/latest/dg/using-composer-project.html)
- Use [AWS SAM](https://aws.amazon.com/serverless/sam/) to build and deploy to AWS:

- - Install [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html), and  [configure it](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config)
- - Install [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- To build and deploy your application for the first time, run the following in your shell:

```bash
sam build
sam deploy --guided
```

For future deploys, you can just run:

```bash
sam build && sam deploy
```

## To Test
- Injest an event into EventBridge with `aws events put-events --entries file://event.json`, which will save it to DynamoDB, and post it to the APIDestination
- Retrieve the event from API Gateway with `curl https://fdgfdg435.execute-api.af-south-1.amazonaws.com/Prod/request/123456789 -H "x-api-key: rtreter5656dgdfg"` where you replace the correct values for the APIGW and APIKEY