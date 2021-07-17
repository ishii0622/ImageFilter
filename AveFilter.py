import cv2
import numpy as np

# load image (grayscale)
# 入力画像をグレースケールで読み込み
color = cv2.imread("./figs/butterfly.png")

# Spatial filtering
# (OpenCVで実装)
dst = cv2.blur(color, ksize=(5, 5))

# output
# 結果を出力
cv2.imwrite("./output/output.png", dst)