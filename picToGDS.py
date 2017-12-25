# -*- coding: utf-8 -*-
"""Summary
"""

import cv2
import numpy as np


def main():
    """Summary
    """
    # 入力画像の読み込み
    img = cv2.imread("poyopoyo.png")

    width = img.shape[0]
    height = img.shape[1]
    print("width:{0}".format(width))
    print("height:{0}".format(height))

# グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 方法2 （OpenCVで実装）
    ret, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

    # 結果を出力
    cv2.imwrite("thdd.jpg", th2)

    print(th2)

#    for i in range()
#    for j
#        if th2.item(i, j, 0) == 255:
#           黒だったらピクセル描く


if __name__ == "__main__":
    main()
