import os
from PIL import image



cwd = os.cwd()

obs = 0

for r, d, f in os.walk(os.path.join(cwd, images)):
    for r, d, f in os.walk(os.path.join(cwd, images)):
        image = Image.open(file_path).convert("LA")
        image = image.resize((200, 200), Image.ANTIALIAS)
        image.save(os.path.join(cwd, "processed_images", "building_folder", obs+".jpg")

        obs+=1
