import os
import pandas as pd
from tqdm import tqdm
import random

image_lists = os.listdir("./trainstan")
data = pd.read_csv("final.csv")




files = list(data["filename"])

"""image_final = random.sample(image_lists, 150000)
for im in tqdm(image_lists):
    if im not in image_final:
        os.remove(os.path.join("./trainstan", im))"""

data = data[data['filename'].isin(image_lists)]

data.to_csv("final_clean.csv", index=None)
