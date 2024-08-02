import cv2

img =  cv2.imread("rash.webp")

resized_img = cv2.resize(img, (600, 700))

#line = cv2.line(img = resized_img,pt1 = (193,81),pt2= (460,81),color = (0,250,0),thickness=2,lineType=cv2.LINE_8)
#cv2.imshow("Rashmika Mandhana", line)

img2 = cv2.putText(img =resized_img, text = "Rashmika",org = (180,63),fontFace=cv2.FACE_RECOGNIZER_SF_FR_COSINE,fontScale=2,color = (0,0,190),thickness=2,lineType=cv2.LINE_8,bottomLeftOrigin=False)

rectangle = cv2.rectangle(img = img2,pt1 = (170,76),pt2= (469,349),color = (0,250,0),thickness=2,lineType=cv2.LINE_8)
cv2.imshow("Rash",rectangle)

cv2.waitKey(0)

cv2.destroyAllWindows()