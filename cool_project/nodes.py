from aineko.core.node import AbstractNode


class CoolNode(AbstractNode):

    def _pre_loop_hook(self, params=None):
        """Optional; used to initialize node state."""
        self.state = params.get("initial_state", 0)

    def _execute(self, params=None):
        """Required; function repeatedly executes."""
        # Implement cool functionality here
        pass
