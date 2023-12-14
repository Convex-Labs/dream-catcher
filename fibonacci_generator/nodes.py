from aineko.core.node import AbstractNode
from typing import Optional

class FibonacciProducer(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        self.state = [0, 1]  # Initialize the first two numbers of the Fibonacci sequence

    def _execute(self, params: Optional[dict] = None) -> None:
        next_value = self.state[-1] + self.state[-2]
        self.producers['fibonacci_output'].produce(next_value)
        self.state.append(next_value)
        if len(self.state) > 2:  # Keep only the last two numbers to save memory
            self.state.pop(0)

class FibonacciConsumer(AbstractNode):
    def _execute(self, params: Optional[dict] = None) -> None:
        message = self.consumers['fibonacci_input'].next()
        if message is not None:
            self.log(f'Received Fibonacci number: {message}', level='info')
