from typing import Optional
from aineko.core.node import AbstractNode
import os
import json
from secrets import SystemRandom

# Node for simulating IoT device data streams

class IoTDataSimulator(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None):
        self.device_ids = params.get('device_ids', [])
        self.location_range = params.get('location_range', {'lat': (0, 90), 'lon': (-180, 180)})
        self.handling_range = params.get('handling_range', (0, 10))
        self.random_gen = SystemRandom()

    def _execute(self, params: Optional[dict] = None):
        for device_id in self.device_ids:
            simulated_data = {
                'device_id': device_id,
                'location': {
                    'latitude': self.random_gen.uniform(*self.location_range['lat']),
                    'longitude': self.random_gen.uniform(*self.location_range['lon']),
                },
                'handling': self.random_gen.uniform(*self.handling_range),
            }
            self.producers['iot_data_stream'].produce(simulated_data)

# Node for detecting crashes or theft based on models

class AlertGenerator(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        message = self.consumers['iot_data_stream'].consume(how='next')
        if message is None:
            return

        data = message['message']
        # Placeholder for actual crash and theft detection logic
        crash_detected = data['handling'] > params.get('crash_threshold', 8)
        theft_detected = data['location']['latitude'] > params.get('theft_latitude_threshold', 80)

        if crash_detected or theft_detected:
            alert = {
                'device_id': data['device_id'],
                'alert_type': 'crash' if crash_detected else 'theft',
                'details': data,
            }
            self.producers['alerts'].produce(alert)
