from aineko.core.node import AbstractNode


class CoolNode(AbstractNode):

    def _pre_loop_hook(self, params=None):
        """Optional; used to initialize node state."""
        self.cool_state = params.get("initial_state", 'cool')

    def _execute(self, params=None):
        """Required; function repeatedly executes."""
        message = self.consumers["cool_input"].next()
        self.log(f"Received input: {message}. Doing something cool...")
        cool_output = f'{message} is now cool!'
        self.producers["cool_output"].produce(cool_output)
