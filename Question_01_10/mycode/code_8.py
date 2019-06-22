import cv2
import numpy as np

def main():
	img = cv2.imread("../imori.jpg")
	for i in range(0, 128, 8):
		for j in range(0, 128, 8):
			img[i:i+8, j:j+8, :] = img[i:i+8, j:j+8, :].max(axis=1).max(axis=0)


	cv2.imwrite("./result_8.jpg", img)

if __name__=="__main__":
	main()
