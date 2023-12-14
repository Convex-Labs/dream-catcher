from aineko.core.node import AbstractNode
from typing import Optional
import time
import os


class LogGeneratorNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        # Simulate log generation with random content using os.urandom for better randomness
        random_value = int.from_bytes(os.urandom(4), 'big') % 100 + 1  # Generates a number between 1 and 100
        log_content = f'INFO: A random event occurred with value {random_value}'
        self.producers['log_stream'].produce(log_content)
        time.sleep(params.get('interval', 1))  # Sleep to simulate log generation interval


class LogProcessorNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        # Process logs from log_stream
        log_message = self.consumers['log_stream'].next()
        if log_message:
            # Placeholder for actual log processing logic
            processed_log = f'Processed log: {log_message}'
            self.producers['processed_log_stream'].produce(processed_log)
            self.log(f'Log processed: {processed_log}', level='info')
