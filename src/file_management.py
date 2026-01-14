import os
import shutil


statis = os.listdir(path="./static")

def clear_public():
    if not os.path.exists("./public"):
        os.mkdir("./public")
        print("Created public directory")
    else:
        public = os.listdir(path="./public")
        shutil.rmtree("./public")
        print("Cleared public directory")
        os.mkdir("./public")
        print("Recreated public directory")




clear_public()