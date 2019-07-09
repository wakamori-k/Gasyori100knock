import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def main():
	img = cv2.imread("../imori_dark.jpg")
	a = 0
	b = 255
	c = img.min()
	d = img.max()
	result_img = img.copy()
	result_img[img<c] = a
	result_img[(img>=c) & (img<=d)] = (b-a)/(d-c) * (result_img[(img>=c) & (img<=d)]-c) + a
	result_img[img>d] = b

	plt.hist(result_img.flatten(), bins=100)
	plt.xlim(0, 255)

	plt.savefig("result_21_hist.png")

	cv2.imwrite("result_21.jpg", result_img)

if __name__=="__main__":
	main()
