from aineko.core.node import AbstractNode
from time import sleep
import logging

class HelloWorldLoggerNode(AbstractNode):
    def _execute(self, params=None):
        logging.info('Hello World')
        sleep(3)
