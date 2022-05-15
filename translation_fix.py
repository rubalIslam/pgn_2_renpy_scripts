import re
import os

cwd = os.getcwd()

file_name = "pgn_events_0.05_tl.rpy"
current_label = "none"

file_name_without_ext=file_name.split(".")[0]+file_name.split(".")[1]

f = open("{fn}_translate.txt".format(fn=file_name_without_ext),"w",encoding="utf-8")

with open(file_name, encoding="utf-8") as trans_file:
    non_blank_trans = [line.strip() for line in trans_file if line.strip()]
    trans_count = 0
    for line in non_blank_trans:
        if "translate" in line:
            label_name = line.split(" ")[2][0:-1]
            #print(label_name[0:-9])
            f.writelines("{} | ".format(label_name[0:-9]))
        if "#" in line and '"' in line:
            #print (line)
            rus_line = line.split('"')
            #print (rus_line[1])
            f.writelines("{} | ".format(rus_line[1]))
        if "#" not in line and '"' in line:
            eng_line = line.split('"')
            #print (eng_line[1])
            f.writelines("{}\n".format(eng_line[1]))
