from aineko.core.node import AbstractNode
from typing import Optional
import secrets


class RandomNumberGenerator(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        """Generate a random number using a secure generator and send it to the output dataset."""
        random_number = secrets.randbelow(101)
        self.producers['random_numbers'].produce(random_number)


class RandomNumberPrinter(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        """Print the random number consumed from the input dataset."""
        random_number = self.consumers['random_numbers'].next()
        self.log(f'Received random number: {random_number}', level='info')
