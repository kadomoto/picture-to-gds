# -*- coding: utf-8 -*-
"""Convert an image file to a GDS file
"""

import sys
import cv2
import numpy as np
import gdspy



def main(fileName, sizeOfTheCell, layerNum):
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

    ret, binaryImage = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

    # Fill orthological corner
    for x in range(width - 1):
        for y in range(height - 1):
            if binaryImage.item(y, x) == 0 and binaryImage.item(y + 1, x) == 255 \
                    and binaryImage.item(y, x + 1) == 255 and binaryImage.item(y + 1, x + 1) == 0:
                binaryImage.itemset((y + 1, x), 0)
            elif binaryImage.item(y, x) == 255 and binaryImage.item(y + 1, x) == 0 \
                    and binaryImage.item(y, x + 1) == 0 and binaryImage.item(y + 1, x + 1) == 255:
                binaryImage.itemset((y + 1, x + 1), 0)

    # Output image.bmp
    cv2.imwrite("image.bmp", binaryImage)
    # The GDSII file is called a library, which contains multiple cells.
    lib = gdspy.GdsLibrary()

    # Geometry must be placed in cells.

    unitCell = lib.new_cell('CELL')
    square = gdspy.Rectangle((0.0, 0.0), (1.0, 1.0), layer=(int)(layerNum))
    unitCell.add(square)

    grid =  lib.new_cell("GRID")

    for x in range(width):
        for y in range(height):
            if binaryImage.item(y, x) == 0:
                print("({0}, {1}) is black".format(x, y))
                cell = gdspy.CellReference(unitCell, origin=(x, height - y - 1))
                grid.add(cell)


    scaledGrid = gdspy.CellReference(
        grid, origin=(0, 0), magnification=(float)(sizeOfTheCell))



    # Add the top-cell to a layout and save
    top = lib.new_cell("TOP")
    top.add(scaledGrid)
    lib.write_gds("image.gds")


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 4:
        fileName = args[1]
        sizeOfTheCell = args[2]
        layerNum = args[3]
        main(fileName, sizeOfTheCell, layerNum)
    else:
        print(
            "usage: python picToGDS.py <fileName> <sizeOfTheCell[um]> <layerNum>")
        quit()
