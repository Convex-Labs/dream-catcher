from aineko.core.node import AbstractNode
from typing import Optional

class FibonacciNode(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None):
        self.state = {'a': 0, 'b': 1}

    def _execute(self, params: Optional[dict] = None):
        a, b = self.state['a'], self.state['b']
        self.producers['fibonacci_output'].produce(a)
        self.state['a'], self.state['b'] = b, a + b
