# To exit image window, press esc.

import cv2
import numpy as np

def load_img(file_name):
    img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
    # print(img)
    return img

def display_img(image):
    cv2.imshow('Aleksandr Karelin', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def hist_eq(image):
    hist, bins = np.histogram(image.flatten(), bins=256, range=[0,256])
    cdf = hist.cumsum()
    # print(cdf)
    cdf_normalized = cdf * 255 / cdf[-1]
    equalized_image = np.interp(image.flatten(), bins[:-1], cdf_normalized).reshape(image.shape)
    # print(cdf)
    return equalized_image.astype(np.uint8)

def rotate(image, theta):
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), np.degrees(theta), 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    return rotated_image

def edge_detection(image):
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    threshold = 50
    edges = (gradient_magnitude > threshold) * 255
    return edges.astype(np.uint8)

def generate_gaussian(sigma, filter_w, filter_h):
    if filter_w == 1 or filter_h == 1:
        size = max(filter_w, filter_h)
        kernel = np.arange(-size // 2 + 1., size // 2 + 1.)
        gaussian_kernel = np.zeros_like(kernel)
        # print("2",gaussian_kernel)
        for i in range(len(kernel)):
            squared_distance = (kernel[i] / sigma) ** 2
            gaussian_kernel[i] = np.exp(-0.5 * squared_distance) / (sigma * np.sqrt(2 * np.pi))
        return(gaussian_kernel / np.sum(gaussian_kernel))
    else:
        size = max(filter_w, filter_h)
        x = np.arange(-size // 2 + 1., size // 2 + 1.)
        y = np.arange(-size // 2 + 1., size // 2 + 1.)
        gaussian_kernel_2d = np.zeros_like(x)
        for i in range(len(x)):
            squared_distance = (x[i]**2 + y[i]**2) / (2 * sigma**2)
            gaussian_kernel_2d[i] = np.exp(-squared_distance) / (2 * np.pi * sigma**2)
        return gaussian_kernel_2d / np.sum(gaussian_kernel_2d)

def apply_filter(image, kernel, pad_pixels, pad_value):
    if pad_value == 0:
        padded_image = np.pad(image, pad_pixels, mode='constant', constant_values=0)
    else:
        padded_image = np.pad(image, pad_pixels, mode='edge')
    if len(kernel.shape) == 1:
        kernel_reshaped = kernel.reshape((1, -1))  # Reshape to a 2D array
        filtered_image = cv2.filter2D(padded_image, -1, kernel_reshaped, borderType=cv2.BORDER_CONSTANT)
    else:
        filtered_image = cv2.filter2D(padded_image, -1, kernel, borderType=cv2.BORDER_CONSTANT)
    return filtered_image

def median_filtering(image, filter_w, filter_h):
    filtered_image = cv2.medianBlur(image, ksize=max(filter_w, filter_h))
    return filtered_image

