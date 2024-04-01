generate_gaussian(sigma, filter_w, filter_h):
This one is done by first checking the filter sizes to determine its
dimensionality and then the kernel is calulated using an index array
and applying the gaussian formula to every element. The same is done 
for the 2D kernel but the formula is slightly changed.

def apply_filter(image, kernel, pad_pixels, pad_value):
First check what the padding is and then apply it. Then using shape
we can get the kernal size(1D or 2D). Then i used built in functions
to convolv it.

def rotate(image, theta):
i get the image dimensionality. Then rotatematrix2d is used to define 
the transformation. Warpaffine is the acutual rotating of the image.


def edge_detection(image):
The Sobel operators are employed along the x and y directions, 
producing gradient images (sobel_x and sobel_y). The magnitude
of these gradients is computed, and a specified threshold is 
utilized to categorize pixels into edge and non-edge regions
Then edges is values above the threshold are set to 255 (white), and others to 0 (black) 