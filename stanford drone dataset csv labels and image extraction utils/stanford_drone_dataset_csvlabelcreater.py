import pandas as pd
import os
import cv2
from tqdm import tqdm

annotations = os.listdir("./annotations")

allowed = ["Biker", "Pedestrian"]

xmin_l = []
ymin_l = []
xmax_l = []
ymax_l = []
name_id_l = []
label_name_l = []
height_l = []
width_l = []
image_name_l = []
for v in annotations:
    print(v)
    path_vid = os.path.join("./annotations", v)
    list_vid = os.listdir(path_vid)
    for video in tqdm(list_vid):
        path_anno = os.path.join(path_vid, video)
        path_f = os.path.join(path_anno, "annotations.txt")
        file1 = open(path_f, 'r')
        lines = file1.readlines()
        image_name = os.path.join(path_anno, "reference.jpg")
        images_h = cv2.imread(image_name)
        height, width, channels = images_h.shape
        for l in tqdm(lines):
            try:
                lists = l.split(" ")
                label_name = lists[9].split('"')
                label_name = label_name[1]
                if label_name in allowed:

                    xmin = lists[1]
                    ymin = lists[2]
                    xmax = lists[3]
                    ymax = lists[4]
                    name_id = lists[5]

                    f_imgname = "image" + "_" + str(v) + "_" + video + "_" + str(name_id) + ".jpg"
                    #print(label_name)


                    xmin_l.append(xmin)
                    ymin_l.append(ymin)
                    xmax_l.append(xmax)
                    ymax_l.append(ymax)
                    name_id_l.append(name_id)
                    label_name_l.append(label_name)
                    height_l.append(height)
                    width_l.append(width)
                    image_name_l.append(f_imgname)
            except:
               pass


data = {'filename': image_name_l,
        'width':width_l,
        "height": height_l,
        "class": label_name_l,
        "xmin":xmin_l,
        "ymin":ymin_l,
        "xmax": xmax_l,
        "ymax": ymax_l,
         "ids":name_id_l }

# Create DataFrame
df = pd.DataFrame(data)

df.to_csv("final.csv", index=None)
