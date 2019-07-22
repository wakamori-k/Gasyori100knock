import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def main():
	img = cv2.imread("../imori.jpg").astype(np.float)

	h, w, c = img.shape
	a = 1.5

	ah = int(a*h)
	aw = int(a*w)

	#拡大後の座標の大きさの配列を確保
	y = np.arange(ah).repeat(aw).reshape(ah, aw)
	x = np.arange(aw).repeat(ah).reshape(aw, ah).T

	#元画像の座標から拡大後画像の座標へのmapを生成
	y_map = (y / a).astype(int)
	x_map = (x / a).astype(int)
	y_map = np.minimum(y_map, h-2)
	x_map = np.minimum(x_map, w-2)

	dy = y / a - y_map
	dx = x / a - x_map

	dy = np.repeat(np.expand_dims(dy, axis=2), 3, axis=2)
	dx = np.repeat(np.expand_dims(dx, axis=2), 3, axis=2)

	result_img = (1.0-dx)*(1.0-dy)*img[y_map, x_map] + \
				dx*(1.0-dy)*img[y_map, x_map+1] + \
				(1.0-dx)*dy*img[y_map+1, x_map] + \
				dx*dy*img[y_map+1, x_map+1]

	result_img[result_img > 255] = 255
	cv2.imwrite("result_26.jpg", result_img)

if __name__=="__main__":
	main()
