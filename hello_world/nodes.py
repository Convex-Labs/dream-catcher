from aineko.core.node import AbstractNode
from typing import Optional

class HelloWorldNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        """This node outputs 'Hello, World!' to the console."""
        self.log('Hello, World!', level='info')
