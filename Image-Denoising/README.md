# Image De-Noising #
Image De-Noising the process of removing unwanted noise from an image. This is a common feature in most of the editing apps out there.

## Bilateral Filter ##
A bilateral filter is a non-linear, edge-preserving, noise-reducing image smoothing filter. It replaces each pixel's intensity with a weighted average of intensity values from neighboring pixels. A Gaussian distribution can be used to measure this weight. Importantly, the weights are determined not only by the Euclidean distance between pixels, but also by radiometric variations (e.g., range differences, such as color intensity, depth distance, etc.). Sharp edges are retained as a result.

## Gaussian Filter ##
The Gaussian blur functionality is created by blurring (smoothing) an image with a Gaussian function to minimize noise. It is a nonuniform low-pass filter that retains low spatial frequency while reducing image noise and irrelevant information in an image. Typically, it is done by convolving an image with a Gaussian kernel. In a Gaussian blur, the pixels closest to the kernel's core are given more weight than those farther away. This averaging is performed channel by channel, and the average channel values become the filtered pixel's new value. Since larger kernels have more values factored into the average, they can blur the picture more than smaller kernels.

## Mean Filter ##
Mean filtering is a simple method of smoothing images by minimizing the amount of intensity difference between one pixel and the next. It is often used to minimize image noise. Mean filtering replaces of pixel value in an image with the mean (average) value of its neighbors, including itself. This eliminates pixel values that are out of place in their surroundings. Mean filtering is also known as a convolution filter. It, like other convolutions, is based on a kernel, which represents the shape and size of the neighborhood to be sampled when determining the mean.

## Median Filter ##
The median filter analyses each pixel in the image separately and compares it to its neighbors to determine whether or not it is reflective of its surroundings. It replaces the pixel value with the median of neighboring pixel values rather than the mean of those values. The median is determined by first numerically sorting all of the pixel values in the surrounding neighborhood and then replacing the pixel under consideration with the middle pixel value. (If the neighborhood has an even number of pixels, the sum of the two middle pixel values is used).

## Image Sharpening ##
Image Sharpening is a technique in which an image is enhanced that helps bring out fine details and edges. The sharpening depends on the value of the kernel. This allows to change kernel values to increase or decrease the sharpening density of the image.
