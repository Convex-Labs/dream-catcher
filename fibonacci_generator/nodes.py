from aineko.core.node import AbstractNode

class FibonacciProducer(AbstractNode):
    def _pre_loop_hook(self, params=None):
        self.a, self.b = 0, 1
        self.max_iterations = params.get('max_iterations', 10)

    def _execute(self, params=None):
        for _ in range(self.max_iterations):
            self.producers['fibonacci_sequence'].produce(self.a)
            self.a, self.b = self.b, self.a + self.b
        self.activate_poison_pill()


class FibonacciConsumer(AbstractNode):
    def _execute(self, params=None):
        fib_number = self.consumers['fibonacci_sequence'].next()
        self.log(f'Received Fibonacci number: {fib_number}')
