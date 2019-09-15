import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def main():
	img = cv2.imread("../imori.jpg").astype(np.float32)
	h, w, _ = img.shape
	tx = 30
	ty = -30

	#変換後の座標
	y = np.arange(h).repeat(w).reshape((h, w))
	x = np.arange(w).repeat(h).reshape((w, h)).T
	y += ty
	x += tx

	result_img = np.zeros_like(img)
	for i in range(h):
		for j in range(w):
			if 0 <= y[i, j] and y[i, j] < h and 0 <= x[i, j] and x[i, j] < w:
				result_img[i, j] = img[y[i, j], x[i, j]]

	cv2.imwrite("result_28.jpg", result_img.astype(np.uint8))

if __name__=="__main__":
	main()
