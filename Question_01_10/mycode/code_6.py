import cv2
import numpy as np

def main():
	img = cv2.imread("../imori.jpg")
	img_result = np.zeros_like(img)
	img_result[(0 <= img) * (img < 64)] = 32
	img_result[(64 <= img) * (img < 128)] = 94
	img_result[(128<= img) * (img < 192)] = 160
	img_result[(192<= img) * (img < 256)] = 244

	cv2.imwrite("./result_6.jpg", img_result)

if __name__=="__main__":
	main()
