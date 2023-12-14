from aineko.core.node import AbstractNode
from typing import Optional


class NumberGeneratorNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        """Generate a number to be processed."""
        number = params.get('start_number', 1)
        self.producers['generated_number'].produce(number)


class MathOperationNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        """Perform a math operation on the input number."""
        input_number = self.consumers['generated_number'].next()
        operation = params.get('operation', lambda x: x)
        result = operation(input_number)
        self.producers['operation_result'].produce(result)


class ResultCollectorNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        """Collect the result from the math operation and log it."""
        result = self.consumers['operation_result'].next()
        self.log(f'Result of math operation: {result}', level='info')
