# Lambda Scheduler Example

A simple example of running cron jobs on AWS Lambda.

[Video](https://youtu.be/IUna2l6p0nk)

![](https://i.imgur.com/dsmVWUe.png)

[Schedule AWS Lambda Functions Using CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RunLambdaSchedule.html)


------

## Usecase

Here is a python script to fetch the twitter trends for a given location/world.

Uses [python-twitter](https://github.com/bear/python-twitter) library.

```bash
$ pip install python-twitter
```

You will need to go to [developer.twitter.com](https://developer.twitter.com/) and create an app and copy its auth credentials in order to make API requests.

```python
import twitter

api = twitter.Api(consumer_key='your_consumer_key',
                  consumer_secret='your_consumer_secret',
                  access_token_key='your_access_token_key',
                  access_token_secret='your_access_token_secret')

def get_trends(woeid=None):
    trends = api.GetTrendsWoeid(woeid) if woeid else api.GetTrendsCurrent()
    return list(map(lambda x:x.AsDict(), trends)) 
```

## References:

- [Intro to AWS Lambda](https://www.youtube.com/watch?v=sTr30oviyHc)

    ![](https://i.ytimg.com/vi/sTr30oviyHc/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLBPrWRZ0tgX2Gp8YYHHB22-NinHCw)
- [Project Setup using AWS SAM](https://www.youtube.com/watch?v=BiV-kdQbEo0)

    ![](https://i.ytimg.com/vi/BiV-kdQbEo0/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLA3nvay4snGWacbAYWD8yud61L0JA)
- [AWS::Serverless::Function template](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html)
- [AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html)
- [Boto3 S3 Resource](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#bucket)