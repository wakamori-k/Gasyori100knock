import cv2
import numpy as np

def main():
	img = cv2.imread("../imori.jpg")

	coeff = np.array([0.722, 0.7152, 0.2126])
	gray_img = (img * coeff).sum(axis=2).astype(np.uint8)
	sb2max=0
	tmax = 0
	for i in range(256):
		w0 = np.count_nonzero(gray_img>=i) / float(gray_img.size)
		w1 = np.count_nonzero(gray_img<i) / float(gray_img.size)
		if gray_img[gray_img>=i].size > 0:
			m0 = gray_img[gray_img>=i].mean()
		else:
			m0 = 0
		if  gray_img[gray_img<i].size > 0:
			m1 = gray_img[gray_img<i].mean()
		else:
			m1 = 0
		sb2 = w0 * w1 * (m0-m1)**2

		if sb2max < sb2:
			sb2max = sb2
			tmax=i

	bin_img = 255*(gray_img >= tmax)
	cv2.imwrite("./result_4.jpg", bin_img)

if __name__=="__main__":
	main()
