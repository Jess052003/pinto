import os
from pathlib import Path
BASE_DIR = str(Path(__file__).resolve().parent.parent)
def write_file(txt):
    pat = BASE_DIR+"\\polls\\user.txt"
    f=open(pat, "w")
    f.write (txt)
    f.close()

def read_file():
    pat = BASE_DIR+"\\polls\\user.txt"
    f=open(pat, "r")
    res=f.read()
    if res =="verified":
        return True
    return False
   
