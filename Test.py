#Problem1
import cv2
img = cv2.imread('JISOO.jpg', -1)
print('Original Dimension: ',img.shape)
width = int(img.shape[1])
height = int(img.shape[0])
re_width = int((width-height)/2)
re_height = int((height-width)/2)

if width > height:
    crop = img[0:height , re_width:height+re_width]
    print('Resized Dimensions: ',crop.shape)
else:
    crop = img[re_height:width+re_height , 0:width]
    print('Resized Dimensions: ',crop.shape)

cv2.imshow('Image',crop)
cv2.imwrite('JiCrop.jpg',crop)
cv2.waitKey(0)   
cv2.destroyAllWindows()

#Problem2
import cv2
cap = cv2.VideoCapture('ROSE.mp4')
print("WIDTH: {}".format(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("HEIGHT : {}".format(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("LENGTH: {}".format(cap.get(cv2.CAP_PROP_POS_MSEC)))
print("FPS : {}".format(cap.get(cv2.CAP_PROP_FPS)))
print("TOTAL FRAME: {}".format(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
while (True):
    ret,frame = cap.read()
    cv2.imshow('VIDEO',frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

a = 123
b = 456
cat = a+b
print("Test the system for the Gitkraken", cat)
