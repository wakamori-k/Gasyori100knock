import cv2
import numpy as np

def main():
	img = cv2.imread("../imori.jpg")

	coeff = np.array([0.722, 0.7152, 0.2126])
	gray_img = (img * coeff).sum(axis=2).astype(np.uint8)

	bin_img = 255*(gray_img >= 128)

	cv2.imwrite("./result_3.jpg", bin_img)

if __name__=="__main__":
	main()
