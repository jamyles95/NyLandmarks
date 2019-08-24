import os
from PIL import Image



cwd = os.getcwd()
obs = 0

images_path = "images"
process_images_dir = "processed_images"
os.mkdir(os.path.join(cwd, process_images_dir))
image_name="index "
obs=0

for d in os.listdir(os.path.join(cwd, images_path)):
    os.mkdir(os.path.join(cwd, process_images_dir, d))
    for image_path in os.listdir(os.path.join(cwd, images_path, d)):
        try:
            image = Image.open(os.path.join(cwd, images_path, d, image_path))#.convert("LA")
            image = image.resize((200, 200), Image.ANTIALIAS)
            image.save(os.path.join(cwd, process_images_dir, d, image_name+str(obs)+".jpg"))

            obs+=1
        except (OSError, AttributeError) as e:
            pass