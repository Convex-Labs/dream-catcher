from aineko.core.node import AbstractNode


class HelloWorldNode(AbstractNode):
    def _execute(self, params=None):
        """Required; function repeatedly executes."""
        self.log('Hello, World!', level='info')
        # Since this is a simple hello world node, we don't need to consume or produce any data.
        # In a real-world scenario, you would use self.consumers and self.producers here.
        return True  # Return True to keep the node running
