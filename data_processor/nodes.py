from aineko.core.node import AbstractNode
from typing import Optional

class DataTransformer(AbstractNode):

    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        """Optional; used to initialize node state."""
        self.transformation_rule = params.get('transformation_rule', lambda x: x)

    def _execute(self, params: Optional[dict] = None) -> None:
        """Required; function repeatedly executes."""
        input_data = self.consumers['input_stream'].next()
        transformed_data = self.transformation_rule(input_data)
        self.producers['output_stream'].produce(transformed_data)
        self.log(f'Transformed data: {transformed_data}', level='info')


class DataSink(AbstractNode):

    def _execute(self, params: Optional[dict] = None) -> None:
        """Required; function repeatedly executes."""
        output_data = self.consumers['output_stream'].next()
        # Here you would typically write the output data to a database or file system.
        # For demonstration purposes, we'll just log the data.
        self.log(f'Received transformed data: {output_data}', level='info')
