import re
import os

cwd = os.getcwd()

file_name="voyeur_eng_chain.rpy"
#file_name="test.txt"
file_name_without_ext=file_name.split(".")[0]

#f = open("{pwd}\\{fn}rpy.txt".format(fn=file_name_without_ext,pwd=cwd), "w")
f = open("{fn}_script.rpy".format(fn=file_name_without_ext),"w",encoding="utf-8")

main_label = "false"

with open(file_name, encoding="utf-8") as text_file:
    non_blank_lines = [line.strip() for line in text_file if line.strip()]
    for line in non_blank_lines:
        if (main_label == "true"):
            print (line)
            main_label = "false"
            f.writelines("call {}\n".format(line.split(" ")[1]))
        if (line[0] == "#" and line[1] == "=" and main_label == "false"):
            main_label = "true"
        