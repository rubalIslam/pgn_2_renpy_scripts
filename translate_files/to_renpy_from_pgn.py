import re
import os

cwd = os.getcwd()

#file_name = "pgn_events_005_eng.rpy"
current_label = "none"

prev_dialogue = ""

directory = "renpy_files"

f = open("01_label_pgn_label.rpy","a",encoding="utf-8")

for file_name in os.scandir(directory):
    '''
    if (str(file_name).count(".") > 1):
        file_name_without_ext=str(file_name).split(".")[0]+str(file_name).split(".")[1]
        f = open("01_label_{fn}.rpy".format(fn=file_name_without_ext),"w",encoding="utf-8")
    else:
        file_name_without_ext=str(file_name).split(".")[0]
        f = open("01_label_{fn}.rpy".format(fn=file_name_without_ext),"w",encoding="utf-8")
    '''
    with open(file_name, encoding="utf-8") as text_file:
        non_blank_lines = [line.strip() for line in text_file if line.strip()]
        line_count = 0
        for line in non_blank_lines:
            if "label " in line and "$" not in line and "=" not in line and (line.split() != "label"):
                #print (line)
                label_name = line.split(" ")[1][0:-1]
                #print(label_name)
                current_label = label_name
                f.writelines("\n#=########################################################")
                f.writelines("\nlabel {}:\n".format(label_name))
                continue
            if "scene " in line and "$" not in line and "=" not in line and ":" not in line and "if" not in line and "animated" not in line and "(" not in line:
                f.writelines("    {}\n".format(line))
                '''
                if "bg" not in line:
                    f.writelines("    {}\n".format(line))
                    continue
                if "bg" in line:
                    f.writelines("    scene {}\n".format(line.split("bg")[1].strip()))
                '''
            if "scene" in line and "$" not in line and "=" not in line and ":" not in line and "if" not in line and "animated" in line and "(" not in line:
                #f.writelines('    "animation here {}"\n'.format(line.split(" ")[2].strip()))
                f.writelines("    {}\n".format(line))
            if "show " in line and "$" not in line and "=" not in line and ":" not in line and "if" not in line and "animated" not in line and "(" not in line and "screen" not in line:
                f.writelines("    {}\n".format(line))
                continue
            if "label" not in line and "=" not in line and "scene" not in line and "#" not in line and "play sound" and "$" not in line and "imagebutton" not in line and "align" not in line and "null" not in line and ":" not in line and "call" not in line and (line.strip() != "pass") and '"' in line:
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
                                sayer_name_sym = line.split('"')[0].strip().split(' ')[0].strip()
                                sayer_name = "max"
                                if (sayer_name_sym == "mom"):
                                    sayer_name = "mom"
                                if (sayer_name_sym == "k"):
                                    sayer_name = "aunt"
                                if (sayer_name_sym == "l"):
                                    sayer_name = "lisa"
                                if (sayer_name_sym == "a"):
                                    sayer_name = "alice"
                                
                                dialogue_with_out_specialchar = tline.split("|")[2].strip()
                                pattern = r"[^A-Za-z0-9_.' ]+"
                                dialogue_without_special_char = re.sub(pattern, '', dialogue_with_out_specialchar)
                                f.writelines('    {} "{}"\n'.format(sayer_name,dialogue_without_special_char))
                                prev_dialogue = tline.split("|")[2].strip()
                                continue
                    
                    

