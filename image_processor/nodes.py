from aineko.core.node import AbstractNode
from typing import Optional
import cv2
import numpy as np


class ImageReader(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        image_path = self.consumers['input_images'].next()
        image = cv2.imread(image_path)
        self.producers['raw_images'].produce(image)


class ImageResizer(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        image = self.consumers['raw_images'].next()
        resized_image = cv2.resize(image, (params['width'], params['height']))
        self.producers['resized_images'].produce(resized_image)


class ImageGrayscaleConverter(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        image = self.consumers['resized_images'].next()
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.producers['grayscale_images'].produce(grayscale_image)
