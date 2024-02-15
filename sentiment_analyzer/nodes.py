from aineko.core.node import AbstractNode
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalysisNode(AbstractNode):

    def _execute(self, params=None):
        """Perform sentiment analysis on the input text."""
        input_text = self.consumers['input_text'].next()
        analyzer = SentimentIntensityAnalyzer()
        sentiment = analyzer.polarity_scores(input_text)
        sentiment_category = 'neutral'
        if sentiment['compound'] >= 0.05:
            sentiment_category = 'positive'
        elif sentiment['compound'] <= -0.05:
            sentiment_category = 'negative'
        self.producers['sentiment_result'].produce({
            'input_text': input_text,
            'sentiment': sentiment_category
        })
