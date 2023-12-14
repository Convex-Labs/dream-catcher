from aineko.core.node import AbstractNode
from typing import Optional
import requests
import time


class APILoadTester(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        """Initialize the API load tester with target URL and load parameters."""
        self.target_url = params.get('target_url')
        self.request_count = params.get('request_count', 100)
        self.concurrency_level = params.get('concurrency_level', 1)
        self.request_interval = params.get('request_interval', 1)  # in seconds
        self.timeout = params.get('timeout', 5)  # default timeout for requests in seconds

    def _execute(self, params: Optional[dict] = None) -> None:
        """Simulate load on the API by sending requests."""
        for _ in range(self.concurrency_level):
            for _ in range(self.request_count):
                try:
                    response = requests.get(self.target_url, timeout=self.timeout)
                    self.producers['api_responses'].produce({
                        'status_code': response.status_code,
                        'response_time': response.elapsed.total_seconds()
                    })
                except requests.exceptions.RequestException as e:
                    self.log(f'Request failed: {e}', level='error')
                time.sleep(self.request_interval)
