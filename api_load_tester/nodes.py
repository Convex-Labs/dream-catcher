from aineko.core.node import AbstractNode
from typing import Optional
import requests
import time


class APILoadTester(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        """Initialize the API load tester node."""
        self.api_url = params.get('api_url')
        self.request_count = params.get('request_count', 100)
        self.request_interval = params.get('request_interval', 1)
        self.timeout = params.get('timeout', 5)  # Default timeout set to 5 seconds

    def _execute(self, params: Optional[dict] = None) -> Optional[bool]:
        """Execute the API load test."""
        for _ in range(self.request_count):
            try:
                response = requests.get(self.api_url, timeout=self.timeout)
                self.producers['api_responses'].produce({'status_code': response.status_code, 'response_time': response.elapsed.total_seconds()})
            except requests.Timeout:
                self.producers['api_responses'].produce({'status_code': 'timeout', 'response_time': self.timeout})
            time.sleep(self.request_interval)
        return True
