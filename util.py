from json import*
FILE_NAME="stud.json"

def read_json():
    with open (FILE_NAME) as f:
        data=load(f)
    return data  

def write_json(data):
    with open (FILE_NAME,"w") as f:
        dump(data,f,indent=3)
              