import cv2
import numpy as np
import math

def main():
	ksize = 3 # kernel size
	padsize = ksize//2 # padding size
	sigma = 1.3 # std. dev.
	kernel = np.ones((ksize, ksize), dtype=float) / (sigma * math.sqrt(2*math.pi))

	for i in range(ksize):
		for j in range(ksize):
			x = i-int(ksize/2)
			y = j-int(ksize/2)
			kernel[i, j] *= math.exp(-(x**2 + y**2) / (2*(sigma**2)))

	kernel /= kernel.sum()

	img = cv2.imread("../imori_noise.jpg")
	img_pad = np.zeros((img.shape[0]+padsize*2, img.shape[1]+padsize*2, img.shape[2]))
	img_pad[padsize:padsize+img.shape[0], padsize:padsize+img.shape[1], :] += img
	img_filtered = np.empty_like(img_pad)
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			for c in range(img.shape[2]):
				img_filtered[i+padsize, j+padsize, c] = (img_pad[i:i+ksize, j:j+ksize, c] * kernel).sum().astype(np.uint8)

	img_filtered = img_filtered[padsize:padsize+img.shape[0], padsize:padsize+img.shape[1], :]
	cv2.imwrite("./result_9_{}.jpg".format(ksize), img_filtered)

if __name__=="__main__":
	main()
