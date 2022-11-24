import os

input_dir = input("Input Directory Path: ")
class_type = str(input("Type of the class: "))

def image_name_generator(input_dir, class_type):
    for dir, subdirs, files in os.walk(input_dir):
        i = 0
        for f in files:
            f_new = f"{class_type}_{str(i)}.jpeg"
            os.rename(os.path.join(dir, f), os.path.join(dir, f_new))
            i += 1
            # print(f, f_new)

image_name_generator(input_dir, class_type)