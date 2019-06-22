import cv2
import numpy as np

def main():
	img = cv2.imread("../imori.jpg")

	coeff = np.array([0.722, 0.7152, 0.2126])
	gray_img = (img * coeff).sum(axis=2).astype(np.uint8)

	cv2.imwrite("./result_2.jpg", gray_img)

if __name__=="__main__":
	main()
