from aineko.core.node import AbstractNode
from typing import Optional
import secrets


class SecureDataSimulatorNode(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        self.data_range = params.get('data_range', (0, 100))

    def _execute(self, params: Optional[dict] = None) -> None:
        # Using secrets module for secure random number generation
        simulated_data = secrets.randbelow(self.data_range[1] - self.data_range[0]) + self.data_range[0]
        self.producers['secure_simulated_data_stream'].produce(simulated_data)
        self.log(f'Produced secure simulated data: {simulated_data}', level='info')


class CoolProcessorNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None) -> None:
        data = self.consumers['secure_simulated_data_stream'].next()
        cool_data = data * 42  # Example of a 'cool' transformation
        self.producers['cool_data_stream'].produce(cool_data)
        self.log(f'Processed data into cool data: {cool_data}', level='info')
