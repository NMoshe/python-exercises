# resize images in cwd and add logo to each of them
import os
from PIL import Image

NEW_SIZE = 300
LOGO = 'catlogo.png'

logoImage = Image.open(LOGO)
logoImage2 = logoImage.resize((int(100), int(100)))
logoWidth = logoImage2.size[0]
logoHeight = logoImage2.size[1]

os.makedirs('withLogo', exist_ok=True)

# Loop files in working directory
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO:
        continue

    image = Image.open(filename)
    width = image.size[0]
    height = image.size[1]

    # check if image needs to be resized
    if width > NEW_SIZE and height > NEW_SIZE:
        # calculate new width and height
        if width > height:
            height = int((NEW_SIZE / width) * height)
            width = NEW_SIZE
        else:
            width = int((NEW_SIZE / height) * width)
            height = NEW_SIZE

        # Resize image
        print(f'Resizing {filename}...')
        image = image.resize((width, height))

    # Add logo
    print(f'Adding logo to {filename}...')
    image.paste(logoImage2, (width - logoWidth, height - logoHeight), logoImage2)

    # save changes
    image.save(os.path.join('withLogo', filename))
