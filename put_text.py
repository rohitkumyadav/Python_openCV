import cv2

imggg  = cv2.imread("salmon.jpg")
imggg = cv2.resize(imggg,(800,700))

img2 = cv2.putText(img =imggg, text = "Salmon bhai",org = (76,93),fontFace=cv2.FACE_RECOGNIZER_SF_FR_COSINE,fontScale=3,color = (128,0,0),thickness=3,lineType=cv2.LINE_8,bottomLeftOrigin=False)
cv2.imshow("Salmon", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()