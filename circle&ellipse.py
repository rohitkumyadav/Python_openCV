import cv2

o_img =  cv2.imread("salmon.jpg")

new_img = cv2.circle(img=o_img,center=(278,116),radius=100,color= (0,0,255),thickness=2,lineType=cv2.LINE_8)
#new_img2  =cv2.ellipse(img = o_img, center= (278,116), axes: Size, angle: float, startAngle: float, endAngle: float, color: Scalar, thickness: int = ..., lineType:)


cv2.imshow("Salmon bhai",new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
