#Problem1
import cv2
cap = cv2.VideoCapture('ROSE.mp4')
def getFrame(sec):
    cap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = cap.read()
    if hasFrames:
        cv2.imwrite("image"+str(count)+".jpg", image)
    return hasFrames
sec = 0
frameRate = 0.5 
count = 1
done = getFrame(sec)
while done:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    done = getFrame(sec)

#Problem2
import cv2
import glob

path = glob.glob(r"C:\Users\ASUS\Desktop\DeepLearning\*.jpg")
path2 = glob.glob(r"C:\Users\ASUS\Desktop\DeepLearning\*.png")
count = 0

for file in path:
    img = cv2.imread(file)
    count += 1
for file in path2:
    img = cv2.imread(file)
    count += 1

name= []
for file in glob.glob('*.jpg'):
    name.append(file)
for file in glob.glob('*.png'):
    name.append(file)

print("Total images: ", count)
print(name)

#Problem3.1 - Grayscale
import cv2
import glob
path = glob.glob(r"C:\Users\ASUS\Desktop\DeepLearning\*.jpg")
path2 = glob.glob(r"C:\Users\ASUS\Desktop\DeepLearning\*.png")
count = 1

for file in path:
    img = cv2.imread(file)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("GrayImage"+str(count)+".jpg", gray)
    count += 1
for file in path2:
    img = cv2.imread(file)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("GrayImage"+str(count)+".jpg", gray)
    count += 1

#Problem3.2 - Calculation and plotting
import glob
import cv2
import matplotlib.pyplot as plt 
path = glob.glob(r"C:\Users\ASUS\Desktop\DeepLearning\GrayImage\*.jpg")
result_avg = []
num = []
for i in path:
    img = cv2.imread(i)
    a = cv2.sumElems(img)[0]
    b = img.size
    avg = round((a/b),3)
    result_avg.append(avg)
for j in range(1,71):
    num.append(j)

plt.plot(num,result_avg,'o')
plt.xlabel("Sequence of GrayImage")
plt.ylabel("Average Intensity")
plt.show()