from aineko.core.node import AbstractNode
import os
import tweepy
from typing import Optional


class TwitterScraperNode(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

        self.query = params.get('query', '#trending')
        self.lang = params.get('lang', 'en')
        self.result_type = params.get('result_type', 'mixed')
        self.count = params.get('count', 100)

    def _execute(self, params: Optional[dict] = None) -> None:
        tweets = self.api.search(q=self.query, lang=self.lang, result_type=self.result_type, count=self.count)
        for tweet in tweets:
            self.producers['scraped_tweets'].produce({'text': tweet.text, 'user': tweet.user.screen_name, 'created_at': str(tweet.created_at)})


class TrendIdentifierNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None) -> None:
        tweet_data = self.consumers['scraped_tweets'].consume()
        if tweet_data is None:
            return

        # Placeholder for trend identification logic
        # For the purpose of this example, we'll just log the tweet
        self.log(f"Identified tweet: {tweet_data['text']} by user {tweet_data['user']} at {tweet_data['created_at']}")
