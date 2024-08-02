import cv2

img = cv2.imread("salmon.jpg")  # image read
img2 = cv2.imread("rash.webp")

cv2.imshow("Salmon bhai",img)   # image show
cv2.imshow("Rashmika Mandhana",img2)

cv2.waitKey(0)    # image facem wait -- time in ms | or press any key command {0}
# if you want to close  only one window then give the name as 
#cv2.destroyWindow("Rashmika Mandhana")

cv2.destroyAllWindows()