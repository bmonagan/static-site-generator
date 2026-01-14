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

def copy_static_to_public():
    clear_public()
    for item in statis:
        print(f"Copying {item} from static to public")
        s = os.path.join("./static", item)
        d = os.path.join("./public", item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)


copy_static_to_public()