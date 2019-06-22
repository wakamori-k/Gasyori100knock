import cv2
import numpy as np
import math

def main():
	kernel_v = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float)
	kernel_h = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float)

	ksize = 3 # kernel size
	padsize = ksize//2 # padding size

	img = cv2.imread("../imori.jpg")
	coeff = np.array([0.722, 0.7152, 0.2126])
	gray_img = (img * coeff).sum(axis=2).astype(np.float)

	gray_img_pad = np.zeros((gray_img.shape[0]+padsize*2, gray_img.shape[1]+padsize*2))
	gray_img_pad[padsize:padsize+img.shape[0], padsize:padsize+img.shape[1]] += gray_img
	gray_img_filtered_v = np.empty_like(gray_img_pad)
	gray_img_filtered_h = np.empty_like(gray_img_pad)
	for i in range(gray_img.shape[0]):
		for j in range(gray_img.shape[1]):
			gray_img_filtered_v[i+padsize, j+padsize] = (gray_img_pad[i:i+ksize, j:j+ksize]*kernel_v).sum()
			gray_img_filtered_h[i+padsize, j+padsize] = (gray_img_pad[i:i+ksize, j:j+ksize]*kernel_h).sum()

	gray_img_filtered_v[gray_img_filtered_v<0] = 0
	gray_img_filtered_v[gray_img_filtered_v>255] = 255
	gray_img_filtered_h[gray_img_filtered_h<0] = 0
	gray_img_filtered_h[gray_img_filtered_h>255] = 255
	gray_img_filtered_v = gray_img_filtered_v[padsize:padsize+gray_img.shape[0], padsize:padsize+gray_img.shape[1]].astype(np.uint8)
	gray_img_filtered_h = gray_img_filtered_h[padsize:padsize+gray_img.shape[0], padsize:padsize+gray_img.shape[1]].astype(np.uint8)
	cv2.imwrite("./result_16_v.jpg", gray_img_filtered_v)
	cv2.imwrite("./result_16_h.jpg", gray_img_filtered_h)

if __name__=="__main__":
	main()
