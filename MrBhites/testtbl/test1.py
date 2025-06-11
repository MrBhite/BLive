def show():
    print("test")


import os, sys
now_dir = os.getcwd()
sys.path.append(now_dir)
sys.path.append("%s/MrBhites/GPT_SoVITS" % (now_dir))