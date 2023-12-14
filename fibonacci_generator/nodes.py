from aineko.core.node import AbstractNode
from typing import Optional


class FibonacciProducer(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        self.state = [0, 1]  # Initialize the Fibonacci sequence

    def _execute(self, params: Optional[dict] = None) -> Optional[bool]:
        next_value = self.state[-1] + self.state[-2]
        self.producers['fibonacci_sequence'].produce(next_value)
        self.state.append(next_value)
        if len(self.state) > 100:  # Limit the sequence to 100 numbers
            self.activate_poison_pill()


class FibonacciConsumer(AbstractNode):
    def _execute(self, params: Optional[dict] = None) -> Optional[bool]:
        message = self.consumers['fibonacci_sequence'].next()
        if message is not None:
            self.log(f'Received Fibonacci number: {message}', level='info')
