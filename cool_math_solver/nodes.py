from aineko.core.node import AbstractNode
import ast


class CoolMathProblemSolver(AbstractNode):

    def _pre_loop_hook(self, params=None):
        """Optional; used to initialize node state."""
        self.problem = params.get("problem", "2 + 2")

    def _execute(self, params=None):
        """Required; function repeatedly executes."""
        # Assuming the problem is a simple arithmetic expression
        try:
            # Using ast.literal_eval for safe evaluation of the expression
            result = ast.literal_eval(self.problem)
            self.log(f'Solving math problem: {self.problem} = {result}')
            self.producers["math_solution"].produce({'solution': result})
        except Exception as e:
            self.log(f'Error solving math problem: {str(e)}', level='error')
            self.activate_poison_pill()

