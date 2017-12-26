# -*- coding: utf-8 -*-
"""Convert image files to GDS files
"""

import cv2
import numpy as np
from gdsCAD import *


def via(w1, w2):
    """Summary
    Args:
        w1 (TYPE): Description
        w2 (TYPE): Description
    Returns:
        TYPE: Description
    """
    cell = core.Cell('VIA')
    square = shapes.Rectangle((0.0, 0.0), (1.0, 1.0), layer=3)
    d = (w1, w2)
    cell.add(utils.translate(square, d))

    return cell


def main():
    """Summary
    """
    # Read an image file
    img = cv2.imread("poyopoyo.jpg")

    width = img.shape[0]
    height = img.shape[1]
    print("width:{0}".format(width))
    print("height:{0}".format(height))

    # Convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    ret, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

    # Output results
    cv2.imwrite("image.bmp", th2)

    print(th2)

    grid = core.Cell('GRID')

    print(th2.item(1, 1))

    for i in range(width):
        for j in range(height):
            if th2.item(j, i) == 0:
                print("({0}, {1}) is black".format(i, j))
                grid.add(via(i, height - j - 1))

    # Add the copied cell to a Layout and save
    layout = core.Layout('LIBRARY')
    layout.add(grid)
    layout.save('image.gds')


if __name__ == "__main__":
    main()
