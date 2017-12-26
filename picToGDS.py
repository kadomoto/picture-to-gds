# -*- coding: utf-8 -*-
"""Convert an image file to a GDS file
"""

import sys
import cv2
import numpy as np
from gdsCAD import *


def unit_cell(x, y):
    """Make a unit-cell

    Args:
        w1 (float): x-position of the via
        w2 (float): y-position of the via
    Returns:
        cell: Description
    """
    cell = core.Cell('VIA')
    square = shapes.Rectangle((0.0, 0.0), (1.0, 1.0), layer=3)
    d = (x, y)
    cell.add(utils.translate(square, d))

    return cell


def main(fileName):
    """Convert an image file (fileName) to a GDS file
    """
    print("Convert an image file to a GDS file.")
    # Read an image file
    img = cv2.imread(fileName)

    width = img.shape[1]
    height = img.shape[0]
    print("width:{0}".format(width))
    print("height:{0}".format(height))

    # Convert an image to grayscale one
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    ret, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

    # Output image.bmp
    cv2.imwrite("image.bmp", th2)

    grid = core.Cell("GRID")

    for i in range(width):
        for j in range(height):
            if th2.item(j, i) == 0:
                print("({0}, {1}) is black".format(i, j))
                grid.add(unit_cell(i, height - j - 1))

    # Add the copied cell to a layout and save
    layout = core.Layout("LIBRARY")
    layout.add(grid)
    layout.save("image.gds")


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        fileName = args[1]
        main(fileName)
    else:
        print("usage: picToGDS.py <fileName>")
        quit()
