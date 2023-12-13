from aineko.core.node import AbstractNode
import os
import tweepy


class TwitterScraperNode(AbstractNode):
    def _pre_loop_hook(self, params=None):
        auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'], os.environ['TWITTER_API_SECRET'])
        auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_SECRET'])
        self.api = tweepy.API(auth)

    def _execute(self, params=None):
        trends = self.api.trends_place(1)  # 1 for worldwide
        self.producers['trends_data'].produce(trends)


class TrendIdentifierNode(AbstractNode):
    def _execute(self, params=None):
        trends_data = self.consumers['trends_data'].consume()
        if trends_data is None:
            return
        identified_trends = self.identify_trends(trends_data)
        self.producers['identified_trends'].produce(identified_trends)

    def identify_trends(self, trends_data):
        trends_list = trends_data[0]['trends']
        return [trend['name'] for trend in trends_list if trend['tweet_volume'] is not None]
