from aineko.core.node import AbstractNode


class HelloWorldNode(AbstractNode):
    def _execute(self, params=None):
        """Required; function repeatedly executes."""
        self.log('Hello, World!', level='info')
        # Since this node doesn't consume or produce to any dataset,
        # we don't need to implement any consume/produce logic.
        # This node simply logs 'Hello, World!' to the console.
