import cv2

img = cv2.imread("salmon.jpg")



new_image = cv2.Canny(img,300,300)

cv2.imshow("Canny", img)
cv2.imshow("Salmon Bhai",new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()