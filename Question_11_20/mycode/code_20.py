import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def main():
	img = cv2.imread("../imori_dark.jpg")

	plt.hist(img.flatten(), bins=100)
	plt.xlim(0, 255)

	plt.savefig("result_20.png")

if __name__=="__main__":
	main()
