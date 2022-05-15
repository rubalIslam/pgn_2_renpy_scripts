import re
import os

cwd = os.getcwd()

directory = "script_files"


#file_name = "script_files/breakfast_eng_chain_script.rpy"
w = open("script_list.txt","w",encoding="utf-8")

for file_name in os.scandir(directory):
    with open(file_name, encoding="utf-8") as text_file:
        non_blank_lines = [line.strip() for line in text_file if line.strip()]
        line_count = 0 
        for line in non_blank_lines:
            f = open(file_name, encoding="utf-8")
            lines = f.readlines()
            try:
                #print (lines[line_count]+":"+str(line_count))
                w.writelines(str(line_count)+"|"+str(lines[line_count]))
            except:
                continue
            line_count += 1

label_list = []
label_dict = {}

file_count = 0
'''
for file_name in os.scandir(directory):
    #print (file_name)
    
    f = open(file_name, encoding="utf-8")
    lines = f.readlines()
    #print (lines[0])

    line_count = 0
    label_list = []
    with open(file_name, encoding="utf-8") as text_file:
        non_blank_lines = [line.strip() for line in text_file if line.strip()]
        for line in non_blank_lines:
            #label_list.append(line)
            #print(line)
            label_dict[line_count] = [line]
            line_count +=1
            #print(file_count)
    file_count +=1

print (label_dict)
'''