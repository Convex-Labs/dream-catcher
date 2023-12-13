from aineko.internals.node import AbstractNode
import random
import ast


class MathPuzzleNode(AbstractNode):
    def _execute(self, params=None):
        # Generate two random numbers for the math puzzle
        num1 = random.SystemRandom().randint(1, 100)
        num2 = random.SystemRandom().randint(1, 100)

        # Randomly choose an operation
        operations = ['+', '-', '*', '/']
        operation = random.SystemRandom().choice(operations)

        # Create the puzzle string
        puzzle = f'{num1} {operation} {num2}'

        # Calculate the answer using a safe method
        answer = str(ast.literal_eval(puzzle))

        # Produce the puzzle and answer
        self.producers['math_puzzle'].produce({'puzzle': puzzle, 'answer': answer})
        self.log(f'Generated puzzle: {puzzle} = {answer}', level='info')

        # Return True to indicate the node should continue running
        return True
