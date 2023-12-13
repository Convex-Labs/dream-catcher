from aineko.core.node import AbstractNode
import tweepy
import os
from collections import Counter
from typing import Optional


class TwitterScraperNode(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        self.api_key = os.getenv('TWITTER_API_KEY')
        self.api_secret_key = os.getenv('TWITTER_API_SECRET_KEY')
        self.access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self.access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        auth = tweepy.OAuthHandler(self.api_key, self.api_secret_key)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)

    def _execute(self, params: Optional[dict] = None) -> Optional[bool]:
        query = params.get('query', '#trending')
        count = params.get('count', 100)
        tweets = self.api.search_tweets(q=query, count=count)
        self.producers['scraped_tweets'].produce({'tweets': [tweet.text for tweet in tweets]})


class TrendIdentifierNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None) -> Optional[bool]:
        tweets_data = self.consumers['scraped_tweets'].consume()
        if tweets_data is None:
            return
        tweets = tweets_data['tweets']
        hashtags = [hashtag for tweet in tweets for hashtag in tweet.split() if hashtag.startswith('#')]
        trends = Counter(hashtags).most_common(10)
        self.producers['identified_trends'].produce({'trends': trends})
