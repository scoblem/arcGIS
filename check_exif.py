import os
from os import path as p
import shutil
from PIL import Image

INPUT = input("Enter source directory: ")
OUTPUT = p.join(INPUT, 'exif_images')
DIR_LIST = os.listdir(INPUT)
FILE_FORMATS = ['.JPG', '.TIF', '.WAV']

supported_files = list()
unsupported_files = list()

for file_name in DIR_LIST:
    if file_name[-4:].upper() in FILE_FORMATS:
        try:
            with Image.open(p.join(INPUT, file_name)) as i:
                i._getexif()
                supported_files.append(file_name)
                print("{} has exif data available.".format(file_name))

        except (AttributeError, OSError) as e:
            unsupported_files.append(file_name)
            print(e)

    else:
        unsupported_files.append(file_name)
        print("{} has no exif data available or is not a valid file type.".format(file_name))

for file_name in supported_files:
    try:
        os.chdir(OUTPUT)
    except FileNotFoundError:
        os.mkdir(OUTPUT)
    finally:
        print("Copying {} to {}".format(file_name, p.basename(OUTPUT)))
        shutil.copy(p.join(INPUT, file_name), p.join(OUTPUT, file_name))

print('Job Done.')
