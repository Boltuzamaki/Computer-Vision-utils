import os
import cv2

path = "./videos"
folder = os.listdir(path)

for f in folder:
    videodir_path = os.path.join(path, f)
    videodir = os.listdir(videodir_path)
    for v in videodir:
        sub_path = os.path.join(videodir_path, v)
        file_path = os.listdir(sub_path)
        for fi in file_path:
            final_path  = os.path.join(sub_path, fi)
            cap= cv2.VideoCapture(final_path)
            print(final_path)
            i=0
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret == False:
                    break
                cv2.imwrite(os.path.join(sub_path  ,  "image" +"_"+ f + "_" + v +"_"+str(i)+ ".jpg") ,frame)
                i+=1

cap.release()
cv2.destroyAllWindows()
