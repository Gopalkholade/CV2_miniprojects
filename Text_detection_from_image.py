import easyocr
import cv2
import os

input_folder="./License Images/"
output_folder="./License Outputs/"

reader = easyocr.Reader(['en'])

for filename in os.listdir(input_folder):
    img = cv2.imread(os.path.join('./License Images/',filename))
    result = reader.readtext(img)
    for detection in result:
        box = detection[0]
        text = detection[1]
        x1,y1=box[0]
        x2,y2=box[1]
        x3,y3=box[2]
        x4,y4=box[3]
        # print(x3,y3)
        # cv2.rectangle(img,(int(x1),int(y1)),(int(x3),int(y3)),(255,255,255),2)
        cv2.rectangle(img,(int(x1),int(y1-20)),(int(x1+100),int(y1)),(255,255,255),-1)
        # img=cv2.putText(img,text,(x1,y1+5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
        cv2.putText(img,text,(int(x1),int(y1-5)),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
    try:
        os.mkdir("License Outputs")
    except:
        pass
    cv2.imwrite(os.path.join(output_folder,filename),img)
print("done")
