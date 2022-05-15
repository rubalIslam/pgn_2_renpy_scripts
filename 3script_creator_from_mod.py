import re
import os

cwd = os.getcwd()

file_name="script_list.txt"
#file_name="test.txt"
file_name_without_ext=file_name.split(".")[0]

#f = open("{pwd}\\{fn}rpy.txt".format(fn=file_name_without_ext,pwd=cwd), "w")
f = open("script_serial.rpy","w",encoding="utf-8")

with open(file_name, encoding="utf-8") as text_file:
        non_blank_lines = [line.strip() for line in text_file if line.strip()]
        for line in non_blank_lines:
            split_line  = line.split("|")
            right_line = split_line[1]
            line_num = split_line[0]
            for line in non_blank_lines:
                if (line_num == line.split("|")[0]):
                    #print (line)
                    f.writelines("{}\n".format(line))
                
