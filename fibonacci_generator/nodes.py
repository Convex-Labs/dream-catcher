from aineko.core.node import AbstractNode
from typing import Optional

class FibonacciProducer(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        self.state = [0, 1]  # Initialize the first two numbers of the Fibonacci sequence

    def _execute(self, params: Optional[dict] = None) -> None:
        next_value = self.state[-1] + self.state[-2]
        self.state.append(next_value)  # Generate the next Fibonacci number
        self.producers['fibonacci_sequence'].produce(next_value)
        self.log(f'Produced Fibonacci number: {next_value}', level='info')


class FibonacciConsumer(AbstractNode):
    def _execute(self, params: Optional[dict] = None) -> None:
        fibonacci_number = self.consumers['fibonacci_sequence'].next()
        self.log(f'Consumed Fibonacci number: {fibonacci_number}', level='info')
        # Here you can add any processing you want to do with the Fibonacci number
