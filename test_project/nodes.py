from aineko.core.node import AbstractNode


class TestNode(AbstractNode):

    def _pre_loop_hook(self, params=None):
        self.log('TestNode initialization.', level='info')

    def _execute(self, params=None):
        test_input = self.inputs['test_input_dataset'].next()
        self.log(f'Received input: {test_input}', level='info')
        test_output = f'Tested: {test_input}'
        self.outputs['test_output_dataset'].write(test_output)
        self.log(f'Output: {test_output}', level='info')