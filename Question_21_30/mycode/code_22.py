import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def main():
	img = cv2.imread("../imori_dark.jpg")
	m0 = 128
	s0 = 52

	result_img = s0/img.std() * (img - img.mean()) + m0

	plt.hist(result_img.flatten(), bins=100)
	plt.xlim(0, 255)

	plt.savefig("result_22_hist.png")

	cv2.imwrite("result_22.jpg", result_img)

if __name__=="__main__":
	main()
