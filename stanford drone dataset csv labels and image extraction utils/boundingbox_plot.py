import pandas as pd
from PIL import Image, ImageDraw

def plotbox(image, csv):
    data = pd.read_csv(csv)
    name_img = image.split("/")[-1]
    print(name_img)
    data = data[data.filename == name_img].reset_index()
    img = Image.open(image)
    print(data)
    for l in range(0 , len(data)):
        xmin =  data["xmin"][l]
        ymin = data["ymin"][l]
        xmax = data["xmax"][l]
        ymax = data["ymax"][l]
        print(xmin, ymin, xmax, ymax)
        shape = [(xmin, ymin), (xmax, ymax)]
        img1 = ImageDraw.Draw(img)
        img1.rectangle(shape, outline ="red")
    img.resize((600, 600))
    img.show()

plotbox("./trainstan/image_hyang_video4_2403.jpg", "final_clean.csv")
