import cv2
import numpy as np
import math

def main():
	kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float)

	ksize = 3 # kernel size
	padsize = ksize//2 # padding size

	img = cv2.imread("../imori.jpg")
	coeff = np.array([0.722, 0.7152, 0.2126])
	gray_img = (img * coeff).sum(axis=2).astype(np.float)
	print(gray_img)

	gray_img_pad = np.zeros((gray_img.shape[0]+padsize*2, gray_img.shape[1]+padsize*2))
	gray_img_pad[padsize:padsize+img.shape[0], padsize:padsize+img.shape[1]] += gray_img

	gray_img_filtered = np.empty_like(gray_img_pad)
	for i in range(gray_img.shape[0]):
		for j in range(gray_img.shape[1]):
			gray_img_filtered[i+padsize, j+padsize] = (gray_img_pad[i:i+ksize, j:j+ksize]*kernel).sum()

	gray_img_filtered[gray_img_filtered<0] = 0
	gray_img_filtered[gray_img_filtered>255] = 255

	gray_img_filtered = gray_img_filtered[padsize:padsize+gray_img.shape[0], padsize:padsize+gray_img.shape[1]].astype(np.uint8)

	cv2.imwrite("./result_17.jpg", gray_img_filtered)

if __name__=="__main__":
	main()
