from aineko.core.node import AbstractNode

class HelloWorldNode(AbstractNode):
    def _execute(self, params=None):
        """This node outputs 'Hello, World!' to the console."""
        self.log('Hello, World!', level='info')
