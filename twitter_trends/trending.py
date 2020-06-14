import twitter

api = twitter.Api(consumer_key='your_consumer_key',
                  consumer_secret='your_consumer_secret',
                  access_token_key='your_access_token_key',
                  access_token_secret='your_access_token_secret')


def get_trends(woeid=None):
    trends = api.GetTrendsWoeid(woeid) if woeid else api.GetTrendsCurrent()
    return list(map(lambda x: x.AsDict(), trends))
