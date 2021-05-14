import pandas as pd
import os
import shutil
import random
from tqdm import tqdm
"""
data = pd.read_csv("final.csv")
data = data.replace(to_replace = "")
data = data.replace(to_replace ="Pedestrian", value ="people")
data = data.replace(to_replace ="Biker", value ="people")


data.to_csv("final_label_clean.csv", index=None)

all_images = os.listdir("./trainstan")
try:
    os.mkdir("train_stan")
    os.mkdir("test_stan")
    os.mkdir("val_stan")
except:
    pass
train = random.sample(all_images, 120000)
new_list = [n for n in tqdm(all_images) if n not in train]
print(len(new_list))
test = random.sample(new_list, 20000)
val = [n for n in tqdm(new_list) if n not in test ]
print(len(val))



for tr in tqdm(train):
    shutil.move(os.path.join("./trainstan", tr), "./train_stan")

for v in tqdm(test):
    shutil.move(os.path.join("./trainstan", v), "./val_stan")

for te in tqdm(val):
    shutil.move(os.path.join("./trainstan", te), "./test_stan")
"""

data = pd.read_csv("final_label_clean.csv")
train = os.listdir("./train_stan")
test = os.listdir("./test_stan")
val = os.listdir("./val_stan")
train_f = data[data['filename'].isin(train)]
train_f.to_csv("train_stanford.csv", index=None)
test_f = data[data['filename'].isin(test)]
test_f.to_csv("test_stanford.csv", index=None)
val_f = data[data['filename'].isin(val)]
val_f.to_csv("val_stanford.csv", index=None)
