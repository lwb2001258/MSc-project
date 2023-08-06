import os
import chemprop
import requests



def download_zinc15_smiles():
    dir_name = "zinc15/raw_data"
    file_list = []
    for i, j, k in os.walk(dir_name):
        file_list.extend(k)
    with open('data/zinc15_uri.txt') as f:
        content = f.readlines()
    for line in content:
        url = line.strip()
        file_name = url.split("/")[-1]
        if file_name in file_list:
            print("pass ", url)
            continue
        req = requests.get(url)
        with open("zinc15/raw_data/"+file_name, "wb") as f:
            f.write(req.content)
        print(url)
download_zinc15_smiles()

