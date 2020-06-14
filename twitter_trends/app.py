import json
import time

import boto3

from trending import get_trends

s3 = boto3.resource('s3')
bucket = s3.Bucket('twitter-trends-bucket')


def _create_key(event):
    return f"{event.get('woeid', 'world')}/{int(time.time())}.json"


def twitter_trends_collector(event, context):
    print(event)
    trends = get_trends(event.get("woeid"))
    bucket.put_object(Key=_create_key(event), Body=json.dumps(trends, indent=2))
    return {"result": "success"}
