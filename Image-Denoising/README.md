# Image De-Noising #
Image De-Noising the process of removing unwanted noise from an image. This is a common feature in most of the editing apps out there.

## Bilateral Filter ##
A bilateral filter is a non-linear, edge-preserving, noise-reducing image smoothing filter. It replaces each pixel's intensity with a weighted average of intensity values from neighboring pixels. A Gaussian distribution can be used to measure this weight. Importantly, the weights are determined not only by the Euclidean distance between pixels, but also by radiometric variations (e.g., range differences, such as color intensity, depth distance, etc.). Sharp edges are retained as a result.

## Mean Filter ##
Mean filtering is a simple method of smoothing images by minimizing the amount of intensity difference between one pixel and the next. It is often used to minimize image noise. Mean filtering replaces of pixel value in an image with the mean (average) value of its neighbors, including itself. This eliminates pixel values that are out of place in their surroundings. Mean filtering is also known as a convolution filter. It, like other convolutions, is based on a kernel, which represents the shape and size of the neighborhood to be sampled when determining the mean.

## Median Filter ##
The median filter analyses each pixel in the image separately and compares it to its neighbors to determine whether or not it is reflective of its surroundings. It replaces the pixel value with the median of neighboring pixel values rather than the mean of those values. The median is determined by first numerically sorting all of the pixel values in the surrounding neighborhood and then replacing the pixel under consideration with the middle pixel value. (If the neighborhood has an even number of pixels, the sum of the two middle pixel values is used).
