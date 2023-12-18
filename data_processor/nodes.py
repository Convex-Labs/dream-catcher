from aineko.core.node import AbstractNode
from typing import Optional

class DataTransformerNode(AbstractNode):

    def _pre_loop_hook(self, params: Optional[dict] = None):
        self.transformation_rule = params.get('transformation_rule', lambda x: x)

    def _execute(self, params: Optional[dict] = None):
        input_data = self.consumers['input_dataset'].next()
        transformed_data = self.transformation_rule(input_data)
        self.producers['output_dataset'].produce(transformed_data)

