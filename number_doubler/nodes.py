from aineko.internals.node import AbstractNode


class NumberGeneratorNode(AbstractNode):
    def _pre_loop_hook(self, params=None):
        """Optional; used to initialize node state."""
        self.start = params.get('start', 0)
        self.end = params.get('end', 10)
        self.current = self.start

    def _execute(self, params=None):
        """Required; function repeatedly executes."""
        if self.current <= self.end:
            self.producers['sequence'].produce(self.current)
            self.current += 1
        else:
            self.activate_poison_pill()


class NumberDoublerNode(AbstractNode):
    def _execute(self, params=None):
        """Required; function repeatedly executes."""
        msg = self.consumers['sequence'].consume()
        if msg is not None:
            doubled_value = msg * 2
            self.producers['doubled_sequence'].produce(doubled_value)
