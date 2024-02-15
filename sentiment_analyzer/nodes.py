from aineko.core.node import AbstractNode
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import openai

openai.api_key = 'your-api-key'


class SentimentAnalyzerNode(AbstractNode):
    def _execute(self, params=None):
        llm_output_text = self.consumers['llm_output'].next()['llm_output_text']
        analyzer = SentimentIntensityAnalyzer()
        sentiment = analyzer.polarity_scores(llm_output_text)
        sentiment_category = 'neutral'
        if sentiment['compound'] >= 0.05:
            sentiment_category = 'positive'
        elif sentiment['compound'] <= -0.05:
            sentiment_category = 'negative'
        self.producers['sentiment_analysis'].produce({'text': llm_output_text, 'sentiment': sentiment_category})
