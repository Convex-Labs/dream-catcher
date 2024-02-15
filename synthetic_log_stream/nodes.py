from aineko.core.node import AbstractNode
from typing import Optional
import json
import os
from datetime import datetime
import secrets


class LogGeneratorNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        # Generate a synthetic log entry using secure random generator
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'log_level': secrets.choice(['INFO', 'WARNING', 'ERROR']),
            'message': f'Synthetic log message with secure random value {secrets.randbelow(100)}'
        }
        # Produce the synthetic log entry to the output dataset
        self.producers['synthetic_log_stream'].produce(log_entry)


class LogProcessorNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        # Consume a synthetic log entry
        log_entry = self.consumers['synthetic_log_stream'].next()
        if log_entry:
            # Process the log entry (e.g., parse, filter, transform)
            processed_entry = f"Processed log entry: {json.dumps(log_entry)}"
            # Produce the processed log entry to the output dataset
            self.producers['processed_log_stream'].produce(processed_entry)
