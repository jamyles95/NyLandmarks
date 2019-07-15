import os
from PIL import Image


cwd = os.getcwd()



for curdir, subdirs, files in os.walk(os.path.join(cwd, "Pictures")):
    print(curdir)
    obs = 0
    filenum = 0
    for sub in subdirs:
        for file in files:
            if file.endswith(".jpg"):
                image = Image.open((curdir  + '\\' + str(file)))
                image = image.resize((200, 200), Image.ANTIALIAS)
                image.save(os.path.join(cwd, "processed_images", "building_folder", str(obs)+".jpg"))
                obs +=1
                filenum +=1
                print("File number " + str(filenum)  + " complete!")
