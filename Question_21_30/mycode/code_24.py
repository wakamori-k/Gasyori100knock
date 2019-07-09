import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def main():
	img = cv2.imread("../imori_gamma.jpg")
	c = 1.0
	g = 2.2
	result_img = img.copy().astype(np.float)

	result_img = (255/c * result_img)**(1/g)

	cv2.imwrite("result_24.jpg", result_img.astype(np.uint8))

if __name__=="__main__":
	main()
