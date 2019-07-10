import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def main():
	img = cv2.imread("../imori.jpg")
	a = 1.5
	result_img = np.zeros((int(img.shape[0]*a), int(img.shape[1]*a), 3))

	for i in range(int(img.shape[0]*a)):
		for j in range(int(img.shape[1]*a)):
			result_img[i, j, :] = img[int(i/a), int(j/a), :]

	cv2.imwrite("result_25.jpg", result_img)

if __name__=="__main__":
	main()
