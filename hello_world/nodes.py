from aineko.core.node import AbstractNode

class HelloWorldNode(AbstractNode):
    def _execute(self, params=None):
        self.log('Hello, World!', level='info')
        self.producers['output'].produce('Hello, World!')
