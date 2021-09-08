import os

image_files = []
os.chdir(os.path.join("OID", "Dataset", "validation"))
for class_name in os.listdir(os.getcwd()):
    if os.path.isdir(class_name):
        os.chdir(class_name)
        for filename in os.listdir(os.getcwd()):
            if filename.endswith(".jpg"):
                image_files.append("data/test/" + filename)
        os.chdir("..")

with open("test.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")
