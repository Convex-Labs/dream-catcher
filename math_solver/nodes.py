from aineko.core.node import AbstractNode
import ast

class MathSolverNode(AbstractNode):

    def _pre_loop_hook(self, params=None):
        pass

    def _execute(self, params=None):
        math_problem = self.consumers['math_problem'].next()
        try:
            # Safely evaluate the math problem as a Python literal
            result = ast.literal_eval(math_problem)
            self.producers['solution'].produce(result)
        except Exception as e:
            self.producers['solution'].produce(f'Error solving math problem: {str(e)}')
