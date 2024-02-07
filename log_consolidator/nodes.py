from aineko.core.node import AbstractNode
from typing import Optional
import requests
import json
import os
from machine_learning_module import UrgencyClassifier

# Define your nodes here

class LogCollector(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        # Collect logs from various sources
        logs = []
        # Example: Fetch logs from a hypothetical API with a timeout
        response = requests.get('http://example.com/api/logs', timeout=5)
        if response.status_code == 200:
            logs.extend(response.json()['logs'])
        # Produce logs for further processing
        self.producers['raw_logs'].produce(logs)

class LogCategorizer(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        # Consume raw logs
        raw_logs = self.consumers['raw_logs'].next()
        if raw_logs:
            # Categorize logs
            classifier = UrgencyClassifier()
            categorized_logs = classifier.categorize(raw_logs)
            # Produce categorized logs
            self.producers['categorized_logs'].produce(categorized_logs)

class SlackNotifier(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        # Consume categorized logs
        categorized_logs = self.consumers['categorized_logs'].next()
        if categorized_logs:
            # Filter urgent logs
            urgent_logs = [log for log in categorized_logs if log['urgency'] == 'high']
            # Send alerts for urgent logs with a timeout
            slack_webhook_url = os.getenv('SLACK_WEBHOOK_URL')
            for log in urgent_logs:
                requests.post(slack_webhook_url, data=json.dumps({'text': log['message']}), headers={'Content-Type': 'application/json'}, timeout=5)
