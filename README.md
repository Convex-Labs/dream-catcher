# Image Processor

The Image Processor project is designed to provide a real-time image processing pipeline. This pipeline is capable of reading images from a stream, resizing them to a specified dimension, and converting them to grayscale.

## Nodes

- `ImageReader`: This node is responsible for reading images from the input stream and producing them to the `raw_images` dataset.
- `ImageResizer`: This node takes the raw images, resizes them according to the specified parameters, and produces the resized images to the `resized_images` dataset.
- `ImageGrayscaleConverter`: This node converts the resized images to grayscale and produces them to the `grayscale_images` dataset.

## Pipeline Design

The pipeline is configured to process images in a sequential manner. Each node in the pipeline is designed to perform a specific task in the image processing workflow. The `input_images` dataset acts as the entry point for the images, which are then passed through the `ImageReader`, `ImageResizer`, and `ImageGrayscaleConverter` nodes in order. The final output is a stream of grayscale images ready for further processing or analysis.