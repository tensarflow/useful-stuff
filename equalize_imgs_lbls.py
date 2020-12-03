import os

# This script works only for the case when image is "image_1.png" and label is "image_1.txt", and there are more labels then images

images_directory = '/home/ensar/ws/dataset_2020-08-11/images'
labels_directory = '/home/ensar/ws/dataset_2020-08-11/labels'

image_files = os.listdir(images_directory)
label_files = os.listdir(labels_directory)
image_filenames_set = set()
label_filenames_set = set()

for image_filename in image_files:
    if image_filename.endswith(".png"):
        image_filename = image_filename.replace(".png", "")
        image_filenames_set.add(image_filename)

for label_filename in label_files:
    if label_filename.endswith(".txt"):
        label_filename = label_filename.replace(".txt", "")
        label_filenames_set.add(label_filename)

differences = list(label_filenames_set - image_filenames_set)

for diff in differences:
    os.remove(labels_directory + "/" + diff + ".txt")