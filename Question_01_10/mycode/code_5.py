import cv2
import numpy as np

def main():
	img = cv2.imread("../imori.jpg")
	img = img.astype(np.float32) / 255.0

	h = np.zeros_like(img[:,:,0]).astype(np.float32) 

	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			Max = img[i, j, :].max().copy()
			Min = img[i, j, :].min().copy()
			b = img[i, j, 0]
			g = img[i, j, 1]
			r = img[i, j, 2]
			if Max == Min:
				h[i, j] = 0.0
			elif Min == b:
				h[i, j] = 60 * (g-r) / (Max - Min) + 60
			elif Min == r:
				h[i, j] = 60 * (b-g) / (Max - Min) + 180
			elif Min==g:
				h[i, j] = 60 * (r-b) / (Max - Min) + 300

	v = img.max(axis=2).copy()
	s = img.max(axis=2).copy() - img.min(axis=2).copy()

	h = (h + 180) % 360

	c = s
	h_dash = h/60.0
	x = c * (1.0-np.abs(h_dash % 2 -1))

	img_after = img
	img_after[:,:,0] = v-c 
	img_after[:,:,1] = v-c 
	img_after[:,:,2] = v-c 
	for i in range(h_dash.shape[0]):
		for j in range(h_dash.shape[1]):
			cij = c[i, j]
			xij = x[i, j]
			if 0 <= h_dash[i, j] and h_dash[i, j] < 1:
				img_after[i, j, :] += np.array([0,xij,cij])
			elif 1 <= h_dash[i, j] and h_dash[i, j] < 2:
				img_after[i, j, :] += np.array([0,cij,xij])
			elif 2 <= h_dash[i, j] and h_dash[i, j] < 3:
				img_after[i, j, :] += np.array([xij,cij,0])
			elif 3 <= h_dash[i, j] and h_dash[i, j] < 4:
				img_after[i, j, :] += np.array([cij,xij,0])
			elif 4 <= h_dash[i, j] and h_dash[i, j] < 5:
				img_after[i, j, :] += np.array([cij, 0, xij])
			elif 5 <= h_dash[i, j] and h_dash[i, j] < 6:
				img_after[i, j, :] += np.array([xij,0,  cij])

	cv2.imwrite("./result_5.jpg", img_after*255)

if __name__=="__main__":
	main()
