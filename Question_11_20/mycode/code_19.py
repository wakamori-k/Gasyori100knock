import cv2
import numpy as np
import math

def main():
	ksize = 5 # kernel size
	padsize = ksize//2 # padding size
	s = 3.0
	kernel = np.empty((ksize, ksize), dtype=np.float)
	for x in range(-padsize, padsize+1):
		for y in range(-padsize, padsize+1):
			kernel[y+padsize, x+padsize] = (x**2 + y**2 - s**2) * np.exp( -(x**2 + y**2) / (2* (s**2)))
	#kernel /= (2 * np.pi * (s**6))
	kernel /= kernel.sum()

	img = cv2.imread("../imori_noise.jpg")
	coeff = np.array([0.0722, 0.7152, 0.2126])
	gray_img = ((img.copy() * coeff).sum(axis=2)).astype(np.uint8)

	gray_img_pad = np.zeros((gray_img.shape[0]+padsize*2, gray_img.shape[1]+padsize*2), dtype=np.float)
	gray_img_pad[padsize:padsize+img.shape[0], padsize:padsize+img.shape[1]] = gray_img.copy().astype(np.float)

	gray_img_filtered = np.empty_like(gray_img_pad)
	for i in range(gray_img.shape[0]):
		for j in range(gray_img.shape[1]):
			gray_img_filtered[i+padsize, j+padsize] = \
				(gray_img_pad[i:i+ksize, j:j+ksize]*kernel).sum()

	gray_img_filtered = gray_img_filtered[padsize:padsize+gray_img.shape[0], padsize:padsize+gray_img.shape[1]].astype(np.uint8)

	cv2.imwrite("./result_19.jpg", gray_img_filtered)

if __name__=="__main__":
	main()
