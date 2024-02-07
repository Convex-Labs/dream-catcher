from aineko.core.node import AbstractNode
import json
import requests
from typing import Optional

# Define your machine learning model for categorization here
# For example, a simple rule-based model could be:
class LogCategorizer(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        log_entry = self.consumers['log_input'].next()
        if log_entry:
            log_data = json.loads(log_entry)
            # Implement your log categorization logic here
            # For simplicity, we're categorizing based on keyword 'error'
            if 'error' in log_data['message'].lower():
                urgency = 'critical'
            else:
                urgency = 'normal'
            log_data['urgency'] = urgency
            self.producers['categorized_log'].produce(json.dumps(log_data))

class SlackNotifier(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        categorized_log_entry = self.consumers['categorized_log'].next()
        if categorized_log_entry:
            log_data = json.loads(categorized_log_entry)
            if log_data['urgency'] == 'critical':
                slack_webhook_url = params['slack_webhook_url']
                slack_message = {
                    'text': f"Critical alert: {log_data['message']}"
                }
                # Fixed Bandit B113 issue by adding a timeout to the request
                response = requests.post(slack_webhook_url, json=slack_message, timeout=10)
                if response.status_code != 200:
                    raise ValueError(f'Error sending Slack notification: {response.text}')