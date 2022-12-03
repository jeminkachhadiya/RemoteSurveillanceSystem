import os

path = input("Enter the path: ")
subject = input("Your search object: ")
# path = r"F:\IMP Folders\Project\GRA\RemoteSurveillanceSystem\yolov7-main\Dataset\1280X720 fit white edge data"
# subject = 2

for dir, subdir, files in os.walk(path):
    for file in files:
        f = open(os.path.join(dir,file), 'r', encoding='utf-8', errors='ignore')
        if dir.split("\\")[-1] == "labels":
            content = f.readlines()
            for c in content:
                if c.startswith(str(subject)):
                    print(os.path.join(dir, file))
