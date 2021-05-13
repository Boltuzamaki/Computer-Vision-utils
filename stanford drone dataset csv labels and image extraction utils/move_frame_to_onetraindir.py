import os
import shutil

path = "./videos"
folder = os.listdir(path)

for f in folder:
    videodir_path = os.path.join(path, f)
    videodir = os.listdir(videodir_path)
    for v in videodir:
        sub_path = os.path.join(videodir_path, v)
        file_path = os.listdir(sub_path)
        for fi in file_path:
            try:
                final_path  = os.path.join(sub_path, fi)
                shutil.move(final_path, path)
            except:
                pass
                
