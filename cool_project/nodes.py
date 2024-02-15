from aineko.core.node import AbstractNode


class CoolNode(AbstractNode):

    def _pre_loop_hook(self, params=None):
        """Optional; used to initialize node state."""
        self.state = params.get('initial_state', 0)

    def _execute(self, params=None):
        """Required; function repeatedly executes."""
        try:
            # Your cool functionality goes here
            # For example, let's say we increment a number and log it
            self.state += 1
            self.log(f'Current state is: {self.state}', level='info')
            # Produce the incremented number to the 'cool_output' dataset
            self.producers['cool_output'].produce(self.state)
        except Exception as err:
            self.log(f'Error occurred in CoolNode: {str(err)}', level='error')
            self.activate_poison_pill()