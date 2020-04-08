import os
import shutil
import glob

# convert tiny-imagenet validation organization into standard imagenet folder organization
VAL_TXT = "/nfs3/data/aniruddha/tiny-imagenet-200/val/val_annotations.txt"
VAL_ROOT = "/nfs3/data/aniruddha/tiny-imagenet-200/val/images/"
VAL_ROOT_FOLDER = VAL_ROOT.replace("images", "images_folder")

os.makedirs(VAL_ROOT_FOLDER)

with open(VAL_TXT, "r") as f:
	lines = f.readlines()

for line in lines:
	elem = line.split()
	if not os.path.exists(os.path.join(VAL_ROOT_FOLDER, elem[1])):
		os.makedirs(os.path.join(VAL_ROOT_FOLDER, elem[1]))

	shutil.copy(os.path.join(VAL_ROOT, elem[0]), os.path.join(VAL_ROOT_FOLDER, elem[1], elem[0]))

# remove txt files from TRAIN folder
TRAIN_ROOT = "/nfs3/data/aniruddha/tiny-imagenet-200/train"
dir_list = glob.glob(TRAIN_ROOT + "/*")

for dir in dir_list:
	txt_file = glob.glob(dir + "/*.txt")
	os.remove(txt_file[0])

