import re
import os

cwd = os.getcwd()
#print(cwd)
test_line = "# | Story Telling only part"
line_with_or = test_line.split("|")
#print (line_with_or[1])
#print (":::",test_line[0])
file_name="voyeur_eng.txt"
#file_name="test.txt"
file_name_without_ext=file_name.split(".")[0]

#f = open("{pwd}\\{fn}rpy.txt".format(fn=file_name_without_ext,pwd=cwd), "w")
f = open("{fn}_chain.rpy".format(fn=file_name_without_ext),"w",encoding="utf-8")

num = ['zero,one,two,three,four,five,six,seven,eight,nine']

menuitem = "false"
label_num = 1
line_num=1
with open(file_name, encoding="utf-8") as text_file:
    non_blank_lines = [line.strip() for line in text_file if line.strip()]
    for line in non_blank_lines:
        if (line[0] == "#" and line[1] != "#") and "|" in line:
            #print (line)
            label_pattern =  r"[^A-Za-z_ ]+"
            label_with_or = line.split("|")
            label_with_lower = str(label_with_or[1]).lower()
            label_with_lower = str(re.sub(label_pattern,'',label_with_lower))
            label_with_lower = label_with_lower.replace(" ","_")
            #label_with_lower = label_with_lower.replace("-","_")
            #print (label_with_lower)
            if (label_num > 1):
                f.writelines('  return\n')
            f.writelines('\n#=##########################################################################\n')    
            f.writelines('\nlabel {}:\n'.format(label_with_lower+str(label_num)+"_"+file_name_without_ext))
            label_num += 1
        if "menuitem:" in line:
            '''
            if "menuitem" in line and (menuitem == "true"):
                print("")
            '''
            if "menuitem" in line and (menuitem == "false"):
                menuitem = "true"
                f.writelines('  menu:\n')
            line_with_power = line.split("^")
            #print (line_with_power[0])
            if (line_with_power[0].count("&") == 1):
                #print (line_with_power[0])
                line_with_and = line_with_power[0].split("&")
                if "!" in line_with_and[1]:
                    #print (line_with_and[1])
                    line_with_not = line_with_and[1].split("!")
                    #menuitem = "false"
                    line_with_or = line_with_power[1].split("|")
                    f.writelines('    "{}":\n'.format(line_with_or[1]))
                    if line_with_not[0][0].isdigit():
                        f.writelines('       "continue"\n') 
                    else:
                        f.writelines('        jump {}\n'.format(line_with_not[0].replace(".","_").replace("-","_")))
                    continue
                if "!" not in line_with_and[1]:
                    #print (line_with_and[1])
                    line_with_or = line_with_power[1].split("|")
                    f.writelines('    "{}":\n'.format(line_with_or[1]))
                    if line_with_and[1][0].isdigit():
                        f.writelines('       "continue"\n')   
                    else:
                        f.writelines('        jump {}\n'.format(line_with_and[1].replace(".","_").replace("-","_")))
                    #menuitem = "false"
                    continue
            if (line_with_power[0].count("&") == 2):
                #print (line_with_power[0])
                line_with_and = line_with_power[0].split("&")
                if "!" in line_with_and[2]:
                    #print (line_with_and[1]).,
                    line_with_not = line_with_and[2].split("!")
                    #menuitem = "false"
                    #print (line_with_not[0])
                    line_with_or = line_with_power[1].split("|")
                    f.writelines('    "{}":\n'.format(line_with_or[1]))
                    if line_with_and[2][0].isdigit():
                        f.writelines('       "continue"\n')   
                        continue 
                    else:
                        f.writelines('        jump {}\n'.format(line_with_not[0].replace(".","_").replace("-","_")))
                    continue
                if "!" not in line_with_and[2]:
                    if "What are you" in line:
                        print ("")
                    #print (line_with_and[2])
                    #menuitem = "false"
                    line_with_or = line_with_power[1].split("|")
                    f.writelines('    "{}":\n'.format(line_with_or[1]))
                    if line_with_and[2][0].isdigit():
                        f.writelines('       "continue"\n')    
                    else:
                        f.writelines('        jump {}\n'.format(line_with_and[2].replace(".","_").replace("-","_")))
                    #print("")
                    continue
            if "^" in line and (line_with_power[0].count("&") == 0):
                line_with_colon = line_with_power[0].split(":")
                line_with_jump = line_with_colon[1].strip()
                line_with_or = line_with_power[1].split("|")
                f.writelines('    "{}":\n'.format(line_with_or[1]))
                #print(line_with_jump)
                if "leave" not in line_with_jump and "!" not in line:
                    if line_with_jump[0].isdigit():
                            f.writelines('       "continue"\n')  
                    else:
                        f.writelines('        jump {}\n'.format(line_with_jump.replace(".","_").replace("-","_")))
                if "leave" not in line_with_jump and "!" in line:
                    if "!" in line_with_jump:
                        line_with_jump_not = line_with_jump.split("!")
                        #print (line_with_jump_not[0])
                        if line_with_jump_not[0][0].isdigit():
                            f.writelines('       "continue"\n') 
                        else:
                            f.writelines('        jump {}\n'.format(line_with_jump_not[0].replace(".","_").replace("-","_")))
                    if "!" not in line_with_jump:
                        #print (line_with_jump)
                        if line_with_jump[0].isdigit():
                            f.writelines('       "continue"\n') 
                        else:
                            f.writelines('        jump {}\n'.format(line_with_jump.replace(".","_").replace("-","_")))
                if "leave" in line_with_jump and "!" not in line:
                    #f.writelines('    "leave"')
                    #print ("leave")
                    f.writelines('        return\n')
                if "leave" in line_with_jump and "!" in line:
                    #print (line_with_colon[1])
                    f.writelines('        return\n')

        if "menuitem:" not in line and (line.count("@") == 2):
            menuitem = "false"
            #print (line)
            line_with_at = line.split("@")
            if "|" in line:
                line_with_or = line.split("|")
                #spoker_num = int(line_with_at[1])
                #print_sayer(spoker_num)
                label_line = line_with_at[0].strip()
                label_line = label_line.replace(".","_")
                #print(label_line)
                f.writelines('\nlabel {}:\n'.format(label_line))
                menuitem = "false"
                dialogue=line_with_or[1].strip()
                dialogue_without_quotes=dialogue.replace('"',"'")
                #print (dialogue_without_quotes)
                f.writelines('  \"{}\"\n'.format(dialogue_without_quotes))
                continue
        if "menuitem:" not in line and (line.count("@") == 3):
            #print (line)
            line_with_at = line.split("@")
            #print(line_with_at[2])
            if "|" in line:
                label_line = line_with_at[0].strip()
                label_line = label_line.replace(".","_")
                #print(label_line)
                f.writelines('\nlabel {}:\n'.format(label_line))
                menuitem = "false"
                line_with_or = line.split("|")
                spoker_num = int(line_with_at[1])
                #print_sayer(spoker_num)
                dialogue=line_with_or[1].strip()
                dialogue_without_quotes=dialogue.replace('"',"'")
                #print (dialogue_without_quotes)
                if "anim" in line_with_at[2]:
                    #print ("skiping animations")
                    print (line_with_at[2])
                    f.writelines('  "animation here {}"\n'.format(line_with_at[2]))
                    continue
                if "anim" not in line_with_at[2]:
                    scene_name = str(line_with_at[2].replace(" ","_"))
                    scene_name = scene_name.replace("'","_")
                    scene_name = scene_name.replace(")","")
                    scene_name = scene_name.replace("(","")
                    scene_name = scene_name.lower()
                    f.writelines("  scene "+scene_name+"\n")
                    #continue
                    f.writelines('  \"{}\"\n'.format(dialogue_without_quotes))
                    continue
