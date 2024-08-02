import cv2

img1 = cv2.imread("salmon.jpg")
img2 = cv2.imread("rash.webp")

img = cv2.resize(img1,(500,600))
img_ = cv2.resize(img2,(500,600))


new_img = cv2.addWeighted(img,0.5,img_,1,1)

cv2.imshow("Salmon bhai",new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()