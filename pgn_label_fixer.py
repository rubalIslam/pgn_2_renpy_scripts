import re
import os

cwd = os.getcwd()

file_name = "pgn_events_0.05.rpy"
current_label = "none"

file_name_without_ext=file_name.split(".")[0]+file_name.split(".")[1]
f = open("{fn}_eng.rpy".format(fn=file_name_without_ext),"w",encoding="utf-8")

with open(file_name, encoding="utf-8") as text_file:
    non_blank_lines = [line.strip() for line in text_file if line.strip()]
    line_count = 0
    for line in non_blank_lines:
        if "label" in line and "$" not in line and "=" not in line:
            #print (line)
            label_name = line.split(" ")[1][0:-1]
            print(label_name)
            current_label = label_name
            f.writelines("#=###############################################\n")
            f.writelines("{}\n".format(line))
        if "label" not in line and "$" not in line and "jump" not in line and ":" not in line and (line.strip() != "pass"):
            f.writelines("    {}\n".format(line))