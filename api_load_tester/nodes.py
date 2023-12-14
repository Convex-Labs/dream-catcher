from aineko.core.node import AbstractNode
from typing import Optional
import requests
import time


class APILoadTester(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        """Initialize the API endpoint and load parameters."""
        self.api_endpoint = params.get('api_endpoint')
        self.request_method = params.get('request_method', 'GET')
        self.request_data = params.get('request_data', None)
        self.request_headers = params.get('request_headers', None)
        self.total_requests = params.get('total_requests', 100)
        self.time_between_requests = params.get('time_between_requests', 1)
        self.timeout = params.get('timeout', 5)  # Default timeout set to 5 seconds

    def _execute(self, params: Optional[dict] = None) -> None:
        """Send requests to the API endpoint to simulate load."""
        for _ in range(self.total_requests):
            try:
                if self.request_method.upper() == 'GET':
                    response = requests.get(self.api_endpoint, headers=self.request_headers, timeout=self.timeout)
                elif self.request_method.upper() == 'POST':
                    response = requests.post(self.api_endpoint, json=self.request_data, headers=self.request_headers, timeout=self.timeout)
                else:
                    self.log(f'Unsupported request method: {self.request_method}', level='error')
                    break

                self.log(f'Request sent. Status code: {response.status_code}', level='info')
            except requests.exceptions.RequestException as e:
                self.log(f'Request failed: {e}', level='error')

            time.sleep(self.time_between_requests)

            if self.consumers['poison_pill'].consume(how='last', timeout=0.1) is not None:
                self.log('Poison pill detected. Terminating load test.', level='info')
                break

