import cv2

def main():
	img = cv2.imread("../imori.jpg")
	img = img.transpose(1, 0, 2)

	cv2.imwrite("result_1.jpg", img)

if __name__=="__main__":
	main()
