import re
import os

cwd = os.getcwd()

file_name = "pgn_events_005_eng.rpy"
current_label = "none"

file_name_without_ext=file_name.split(".")[0]+file_name.split(".")[1]
f = open("01_label_{fn}.rpy".format(fn=file_name_without_ext),"w",encoding="utf-8")
prev_dialogue = ""

with open(file_name, encoding="utf-8") as text_file:
    non_blank_lines = [line.strip() for line in text_file if line.strip()]
    line_count = 0
    for line in non_blank_lines:
        if "label" in line and "$" not in line:
            #print (line)
            label_name = line.split(" ")[1][0:-1]
            #print(label_name)
            current_label = label_name
            f.writelines("\n#=########################################################")
            f.writelines("\nlabel {}:\n".format(label_name))
        if "scene" in line:
            f.writelines("    {}:\n".format(line))
        if "label" not in line and "scene" not in line and "#" not in line and "play sound" and "$" not in line and "imagebutton" not in line and "align" not in line and "null" not in line and ":" not in line and "call" not in line:
            dialogue = line.split('"')[1].strip()
            #print (dialogue)
            
            with open("pgn_events_005_tl_translate.txt", encoding="utf-8") as trans_file:
                non_blank_trans = [lin.strip() for lin in trans_file if lin.strip()]
                tline_count = 0
                for tline in non_blank_trans:
                    if (tline.count("|") == 2):
                        tdialogue = tline.split("|")[1].strip()
                        #print(tdialogue)
                        if (dialogue.strip() == tdialogue.strip() and prev_dialogue != tline.split("|")[2].strip()):
                            f.writelines('    {} "{}"\n'.format(line.split('"')[0].strip(),tline.split("|")[2].strip()))
                            prev_dialogue = tline.split("|")[2].strip()
                    
                    

