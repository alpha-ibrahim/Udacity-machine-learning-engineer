import os
import sys
from PIL import Image
import glob
import shutil

def resize(folder, fileName, factor):
    filePath = os.path.join(folder, fileName)
    im = Image.open(filePath)
    w, h  = im.size
    newIm = im.resize((int(w*factor), int(h*factor)))
    # i am saving a copy, you can overrider orginal, or save to other folder
    #newIm.save(filePath+"copy.png")
    newIm.save(filePath)


def bulkResize(imageFolder, factor):
    imgExts = ["png", "bmp", "jpg"]
    for path, dirs, files in os.walk(imageFolder):
        for fileName in files:
            ext = fileName[-3:].lower()
            if ext not in imgExts:
                continue

            resize(path, fileName, factor)

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def move_to_dir(src_dir,dest_dir):
    for filename in glob.glob(os.path.join(src_dir, '*.*')):
        shutil.move(filename, dest_dir)