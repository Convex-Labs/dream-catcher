from aineko.core.node import AbstractNode
from typing import Optional
import requests
import time


class APILoadTester(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None):
        """Initialize the API endpoint and load parameters."""
        self.api_endpoint = params.get('api_endpoint')
        self.request_method = params.get('request_method', 'get').lower()
        self.request_data = params.get('request_data', None)
        self.request_headers = params.get('request_headers', None)
        self.total_requests = params.get('total_requests', 100)
        self.concurrency_level = params.get('concurrency_level', 1)
        self.timeout_seconds = params.get('timeout_seconds', 5)  # Default timeout set to 5 seconds
        self.requests_made = 0

    def _execute(self, params: Optional[dict] = None):
        """Perform the load test by sending requests to the API endpoint."""
        if self.requests_made >= self.total_requests:
            return

        # Simulate concurrent requests
        for _ in range(self.concurrency_level):
            try:
                if self.request_method == 'get':
                    response = requests.get(self.api_endpoint, headers=self.request_headers, timeout=self.timeout_seconds)
                elif self.request_method == 'post':
                    response = requests.post(self.api_endpoint, data=self.request_data, headers=self.request_headers, timeout=self.timeout_seconds)
                else:
                    self.log(f'Unsupported request method: {self.request_method}', level='error')
                    return

                self.requests_made += 1
                self.log(f'Request {self.requests_made}/{self.total_requests}: Status {response.status_code}', level='info')
            except requests.Timeout:
                self.log('Request timed out', level='warning')

            # Throttle requests if needed
            time.sleep(params.get('throttle_seconds', 0))

            if self.requests_made >= self.total_requests:
                break
