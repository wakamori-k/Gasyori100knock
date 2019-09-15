import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def main():
	_img = cv2.imread("../imori.jpg").astype(np.float32)
	_h, _w, _c = _img.shape
	tx = 30
	ty = -30
	
	# 0パディングを追加
	img = np.zeros((_h+2, _w+2, _c), dtype=np.float32)
	img[1:_h+1, 1:_w+1] = _img
	h, w, _ = img.shape

	# 変換前の座標
	y = np.arange(h).repeat(w).reshape((h, w))
	x = np.arange(w).repeat(h).reshape((w, h)).T

	# 変換後の座標
	y_trans = np.minimum(np.maximum(y + ty, 0), h-1)
	x_trans = np.minimum(np.maximum(x + tx, 0), w-1)

	result_img = np.zeros_like(img)
	result_img[y, x] = img[y_trans, x_trans]

	cv2.imwrite("result_28.jpg", result_img[1:_h+1, 1:_w+1].astype(np.uint8))

if __name__=="__main__":
	main()
