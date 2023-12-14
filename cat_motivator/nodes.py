from aineko.core.node import AbstractNode
from typing import Optional
import time


class CatMotivatorNode(AbstractNode):
    def _pre_loop_hook(self, params: Optional[dict] = None) -> None:
        self.messages = [
            'Paws and reflect on your achievements.',
            'You are purr-fect just the way you are.',
            'Stay positive and curious!',
            'Keep a paws-itive mindset.',
            'You have the courage to go through any hurdle.',
            'Every day is a new oppurrtunity.',
            'Believe in yourself, you are claw-some!'
        ]
        self.message_index = 0

    def _execute(self, params: Optional[dict] = None) -> None:
        time.sleep(3)  # Wait for 3 seconds before generating the next message
        motivational_message = self.messages[self.message_index]
        self.producers['cat_motivation'].produce(motivational_message)
        self.message_index = (self.message_index + 1) % len(self.messages)
        self.log(f'Produced message: {motivational_message}', level='info')
