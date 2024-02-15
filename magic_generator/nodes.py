from aineko.core.node import AbstractNode

class MagicNode(AbstractNode):

    def _pre_loop_hook(self, params=None):
        """Optional; used to initialize node state."""
        self.magic_state = 'Ready to create magic!'

    def _execute(self, params=None):
        """Required; function repeatedly executes."""
        input_data = self.inputs['user_input'].next()
        magic_output = self.perform_magic(input_data)
        self.outputs['magical_output'].write(magic_output)

    def perform_magic(self, input_data):
        """Performs magical transformation on the input data."""
        # Here we simulate a magical transformation
        return f'Magical result for: {input_data}'
