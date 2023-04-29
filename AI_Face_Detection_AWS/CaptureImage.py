####
#conda update anaconda-navigator  
#conda update navigator-updater  
#####3
import cv2

ph = cv2.VideoCapture(1)
print(ph)
ret,photo = ph.read()
print(ret)
if ret:
    cv2.imwrite('test.png',ph)