import cv2
import numpy as np
import os
  # BGR(255,0,0)
img = cv2.imread("rash.webp")
'''resize = cv2.resize(img,(100,150))
v = np.vstack(((resize,resize,resize)))   # vstack > vertical | bstack > horizontal
h = np.hstack(((v,v,v))) '''

#cv2.imshow("Salmon bhai",h)
names = os.listdir(r"/home/superuser/Music")
for name in names:
    path = r"/home/superuser/Music"
    img_name = path +"/" +name
    img = cv2.imread(img_name)
    img = cv2.resize(img,(300,400))
    cv2.imshow("Presentation",img)
    cv2.waitKey(0)  # 1000 millisecond = 1 second
cv2.destroyAllWindows()