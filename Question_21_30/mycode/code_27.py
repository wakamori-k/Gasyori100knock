import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def main():
	img = cv2.imread("../imori.jpg").astype(np.float32)

	h, w, c = img.shape
	a = 1.5

	ah = int(a*h)
	aw = int(a*w)

	#拡大後の座標の大きさの配列を確保
	y = np.arange(ah).repeat(aw).reshape(ah, aw)
	x = np.arange(aw).repeat(ah).reshape(aw, ah).T

	#元画像の座標から拡大後画像の座標へのmapを生成
	y_map = np.floor(y / a).astype(np.int)
	x_map = np.floor(x / a).astype(np.int)
	y_map = np.minimum(y_map, h-1)
	x_map = np.minimum(x_map, w-1)

	dy = []
	dy.append(y / a - (y_map - 1))
	dy.append(y / a - (y_map))
	dy.append((y_map + 1) - y / a)
	dy.append((y_map + 2) - y / a)

	dx = []
	dx.append(x / a - (x_map - 1))
	dx.append(x / a - (x_map))
	dx.append((x_map + 1) - x / a)
	dx.append((x_map + 2) - x / a)

	for i in range(len(dy)):
		dy[i] = np.repeat(np.expand_dims(dy[i], axis=2), 3, axis=2)
		dx[i] = np.repeat(np.expand_dims(dx[i], axis=2), 3, axis=2)

	dy = np.array(dy)
	dx = np.array(dx)

	alpha = -1.0
	fy1 = dy<=1
	fy2 = (1<dy) & (dy<2)
	fx1 = dx<=1
	fx2 = (1<dx) & (dx<2)

	wy = np.zeros_like(dy)
	wx = np.zeros_like(dx)
	wy[fy1] = 1 - (alpha+3)*(dy[fy1]**2) + (alpha+2)*(dy[fy1]**3)
	wx[fx1] = 1 - (alpha+3)*(dx[fx1]**2) + (alpha+2)*(dx[fx1]**3)

	wy[fy2] = -4*alpha + 8*alpha*dy[fy2] - 5*alpha*(dy[fy2]**2) + alpha*(dy[fy2]**3)
	wx[fx2] = -4*alpha + 8*alpha*dx[fx2] - 5*alpha*(dx[fx2]**2) + alpha*(dx[fx2]**3)

	result_img = np.zeros((ah, aw, 3), dtype=np.float)
	w_sum = np.zeros((ah, aw, 3), dtype=np.float)

	for i in range(-1, 3):
		for j in range(-1, 3):
			idx_y = np.minimum(np.maximum(y_map + i, 0), h-1)
			idx_x = np.minimum(np.maximum(x_map + j, 0), w-1)

			w_sum += wy[i+1] * wx[j+1]
			result_img += img[idx_y, idx_x] * wy[i+1] * wx[j+1]

	result_img /= w_sum

	result_img[result_img > 255] = 255
	cv2.imwrite("result_27.jpg", result_img.astype(np.uint8))

if __name__=="__main__":
	main()
