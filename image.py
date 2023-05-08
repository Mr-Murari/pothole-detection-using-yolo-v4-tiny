#importing necessary libraries
import cv2
import os
from tkinter.filedialog import askopenfile

#reading test image
#file=askopenfile(filetypes=[("Image file","*.png")])
img = cv2.imread("C:\\Users\\MURARI\\Desktop\\POTHOLE\\pothole-detection\\p2.jfif") #image name
#img = cv2.imread(file) #image name

#reading label name from obj.names file
with open(os.path.join("C:\\Users\\MURARI\\Desktop\\POTHOLE\\pothole-detection\\project_files",'obj.names'), 'r') as f:
    classes = f.read().splitlines()

#importing model weights and config file
net = cv2.dnn.readNet("C:\\Users\\MURARI\\Desktop\\POTHOLE\\pothole-detection\\project_files\\yolov4_tiny.weights","C:\\Users\\MURARI\\Desktop\\POTHOLE\\pothole-detection\\project_files\\yolov4_tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)
classIds, scores, boxes = model.detect(img, confThreshold=0.6, nmsThreshold=0.4)

#detection 
for (classId, score, box) in zip(classIds, scores, boxes):
    cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                  color=(0, 255, 0), thickness=2)
 
cv2.imshow("pothole",img)
cv2.imwrite("result1"+".jpg",img) #result name
cv2.waitKey(0)
cv2.destroyAllWindows()
