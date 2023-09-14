import cv2
import numpy as np


def stack_images(images, rows, cols, scale):
    """
    Stack multiple images in a grid with the specified number of rows and columns.

    Args:
        images (list): List of images to stack.
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.
        scale (float): Scaling factor for resizing images.

    Returns:
        numpy.ndarray: The stacked image grid.
    """
    width = images[0].shape[1]
    height = images[0].shape[0]

    # Check if there are more images than rows*cols
    if len(images) != rows * cols:
        if rows * cols < len(images):
            print("WARNING: NOT ALL IMAGES WILL BE DISPLAYED SINCE THERE ARE MORE IMAGES THAN ROWS AND COLUMNS")
            images = images[:rows * cols]
        else:
            for _ in range(rows * cols - len(images)):
                images.append(np.zeros((height, width, 3), np.uint8))

    # Resize the images
    resized_images = [cv2.resize(image, (width, height)) for image in images]

    # Scale the images
    scaled_images = [cv2.resize(image, (0, 0), None, scale, scale) for image in resized_images]

    # Convert grayscale images to color
    gray_to_color = []
    for image in scaled_images:
        if len(image.shape) == 2:
            gray_to_color.append(cv2.cvtColor(image, cv2.COLOR_GRAY2BGR))
        else:
            gray_to_color.append(image)

    # Horizontally stack the images in each row
    hor_stack = []
    for i in range(rows):
        hor_stack.append(np.hstack(gray_to_color[i * cols: (i + 1) * cols]))

    # Vertically stack the rows to create the final image grid
    ver_stack = np.vstack(hor_stack)

    return ver_stack

# Example usage:
# stacked_image = stack_images(list_of_images, num_rows, num_cols, scaling_factor)
