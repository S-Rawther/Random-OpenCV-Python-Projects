# Image De-Noising #
Image De-Noising the process of removing unwanted noise from an image. This is a common feature in most of the editing apps out there.

## Bilateral Filter ##
A bilateral filter is a non-linear, edge-preserving, noise-reducing image smoothing filter. It replaces each pixel's intensity with a weighted average of intensity values from neighboring pixels. A Gaussian distribution can be used to measure this weight. Importantly, the weights are determined not only by the Euclidean distance between pixels, but also by radiometric variations (e.g., range differences, such as color intensity, depth distance, etc.). Sharp edges are retained as a result.
