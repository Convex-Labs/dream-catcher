from aineko.core.node import AbstractNode


class AwesomeNode(AbstractNode):

    def _pre_loop_hook(self, params=None):
        """Optional; used to initialize node state."""
        self.state = params.get("initial_state", 'awesome')

    def _execute(self, params=None):
        """Required; function repeatedly executes."""
        # This node doesn't consume any input, it just produces something awesome
        self.producers["awesome_output"].produce({'message': 'This is something awesome!'})
        self.log(f"Produced something awesome", level="info")
