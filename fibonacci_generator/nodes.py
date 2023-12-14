from aineko.core.node import AbstractNode
from typing import Optional

class FibonacciProducer(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        self.state = {'a': 0, 'b': 1}

    def _execute(self, params: Optional[dict] = None) -> None:
        a, b = self.state['a'], self.state['b']
        self.producers['fibonacci_sequence'].produce(a)
        self.state['a'], self.state['b'] = b, a + b

class FibonacciConsumer(AbstractNode):
    def _execute(self, params: Optional[dict] = None) -> None:
        fib_number = self.consumers['fibonacci_sequence'].next()
        self.log(f'Received Fibonacci number: {fib_number}')
