import re
import os
import json

file_name="CommonEvents.json"

json_file=open(file_name)
json_data = json.load(json_file)
file_name_without_ext=file_name.split(".")[0]
f = open("{fn}.rpy".format(fn=file_name_without_ext),"w",encoding="utf-8")
sayers = open("sayer.rpy","w",encoding="utf-8")
movies_file_name = open("movies.rpy","w",encoding="utf-8")


#print (json_data[1]["list"][3])
#use id 256 for testing which has images
count = 0
current_char = ""
prev_dialogue = ""
sayer_list = []
prev_dialogue_for_movie = ""

for i in json_data:
    count+=1
    #print (json_data[count]["name"])
    try:
        if (json_data[count]["name"] != ""):
            label_with_underscore = json_data[count]["name"].replace(" ","")
            if (label_with_underscore == "Timeofday"):
                first_label = str(file_name_without_ext)
                print(first_label)
                f.writelines('\nlabel {}:\n'.format(first_label))
            else:
                pattern = r'[^A-Za-z0-9_]+'
                label_without_special_char = re.sub(pattern, '', label_with_underscore)
                f.writelines('  return \n\nlabel {}:\n'.format(label_without_special_char+"_"+str(file_name_without_ext)))
            for per_list in json_data[count]["list"]:
                #print (per_list)
                if per_list["parameters"]:
                    #print(len(per_list["parameters"]))
                    #if (str(len(per_list["parameters"]) == "1")):
                    #print (":::",per_list["parameters"][0])
                    if (str(len(per_list["parameters"])) == "5"):
                        if type(per_list["parameters"][0]) is list:
                            #print (per_list["parameters"][0])
                            f.writelines('  menu:\n')
                            m_count = 0
                            for menu_items in per_list["parameters"][0]:
                                if (m_count == 0):
                                    menu_name0 = str(menu_items)
                                if (m_count == 1):
                                    menu_name1 = str(menu_items)
                                if (m_count == 2):
                                    menu_name2 = str(menu_items)
                                if (m_count == 3):
                                    menu_name3 = str(menu_items)
                                if (m_count == 4):
                                    menu_name4 = str(menu_items)
                                if (m_count == 5):
                                    menu_name5 = str(menu_items)
                                #menu_name.insert(m_count,menu_items)
                                #print(menu_items)
                                m_count += 1
                                f.writelines('    \"{}\":\n'.format(menu_items))
                                jump_with_underscore = str(menu_items).replace(" ","_")
                                jump_with_underscore = str(menu_items).replace("\\","")
                                pattern = r'[^A-Za-z0-9_]+'
                                jump_without_special_char = re.sub(pattern, '', jump_with_underscore)
                                if not str(jump_without_special_char[0]).isdigit():
                                    f.writelines('      call {}\n'.format(jump_without_special_char))
                                else:
                                    #print (jump_without_special_char)
                                    f.writelines('      call {}\n'.format("m_"+jump_without_special_char))
                    if (str(len(per_list["parameters"])) == "2"):
                        #print (menu_name)  
                        #print(per_list["parameters"][1])
                        #if (str(per_list["parameters"][1]) == str(menu_name[0]) or str(per_list["parameters"][1]) == str(menu_name[1])):
                        if (per_list["parameters"][1] == menu_name0 or per_list["parameters"][1] == menu_name1 or per_list["parameters"][1] == menu_name2 or per_list["parameters"][1] == menu_name3 or per_list["parameters"][1] == menu_name4 or per_list["parameters"][1] == menu_name5):
                            #print (per_list["parameters"][1])
                            label_with_underscore = str(per_list["parameters"][1]).replace(" ","_")
                            label_with_underscore = str(per_list["parameters"][1]).replace("\\","")
                            pattern = r'[^A-Za-z0-9_]+'
                            label_without_special_char = re.sub(pattern, '', label_with_underscore)
                            if not label_without_special_char[0].isdigit():
                                #print (label_without_special_char)
                                f.writelines('label {}:\n'.format(label_without_special_char))
                            else:
                                #print (label_without_special_char)
                                f.writelines('label {}:\n'.format("m_"+label_without_special_char))
                        #else:
                            #print ("else missed::",per_list["parameters"][1])
                            #print ("m1",menu_name1)
                            #print ("m2",menu_name2)
                    if (str(len(per_list["parameters"])) == "1" or str(len(per_list["parameters"])) == "4"):
                        if (str(len(per_list["parameters"])) == "4" and not str(per_list["parameters"][0]).isdigit()):
                            #print (":::",per_list["parameters"][0])
                            current_char = per_list["parameters"][0]

                            if current_char not in sayer_list:
                                sayer_list.append(current_char)
                        if (str(len(per_list["parameters"])) == "1" and not str(per_list["parameters"][0]).isdigit() and per_list["parameters"][0] != ""):
                            #print (":::",per_list["parameters"][0])
                            if (prev_dialogue != per_list["parameters"][0] and "{" not in str(per_list["parameters"][0])):
                                if "Common event 'StopMovie'" in per_list["parameters"][0]:
                                    #print (prev_dialogue)
                                    pattern = r'[^A-Za-z0-9_]+'
                                    movie_name = re.sub(pattern, '',prev_dialogue)
                                    movie_name = movie_name.replace(" ","_")
                                    movie_name = movie_name.lower()
                                    print (movie_name)
                                    movies_file_name.writelines("image {} = Movie(play=\"movies/{}.webm\", channel=\"movie\", size=(1920,1080))\n".format(movie_name,prev_dialogue))
                                    f.writelines('  show {}\n'.format(movie_name))
                                    continue
                                if (current_char.strip() == ""):
                                    dialogue_without_quotes=str(per_list["parameters"][0]).replace('"',"'")
                                    pattern = r'[^A-Za-z0-9_ ]+'
                                    dialogue_without_special_char = re.sub(pattern, '', dialogue_without_quotes)
                                    f.writelines('  \"{}\"\n'.format(dialogue_without_special_char))
                                    prev_dialogue = per_list["parameters"][0]
                                    continue
                                if (current_char.strip() != "" and "{" not in str(per_list["parameters"][0])):
                                    dialogue_without_quotes=str(per_list["parameters"][0]).replace('"',"'")
                                    pattern = r'[^A-Za-z0-9_ ]+'
                                    dialogue_without_special_char = re.sub(pattern, '', dialogue_without_quotes)
                                    if "-" in current_char:
                                        current_char_split = current_char.split("-")
                                        f.writelines('  {}  \"{}\"\n'.format(current_char_split[0],dialogue_without_special_char))
                                        prev_dialogue = per_list["parameters"][0]
                                        continue
                                    if " " in current_char:
                                        current_char_split = current_char.split(" ")
                                        f.writelines('  {}  \"{}\"\n'.format(current_char_split[0],dialogue_without_special_char))
                                        prev_dialogue = per_list["parameters"][0]
                                        continue
                                    if "-" not in current_char and " " not in current_char:    
                                        f.writelines('  {}  \"{}\"\n'.format(current_char,dialogue_without_special_char))
                                        prev_dialogue = per_list["parameters"][0]
                                        continue
                            continue
                    if (str(len(per_list["parameters"])) == "10"):
                        if ( per_list["parameters"][1] != "" and not str(per_list["parameters"][1]).isdigit()):
                            lower_of_scene = per_list["parameters"][1].lower()
                            lower_of_scene = lower_of_scene.replace(" ","_")
                            lower_of_scene = lower_of_scene.replace("'","_")
                            if "missing" not in lower_of_scene:
                                f.writelines("  scene {} \n".format(lower_of_scene))
    except:
        print ("ignoring")
#print (sayer_list)
for sayer in sayer_list:
    if (sayer.strip() != ""):
        if "-" in sayer:
            sayer_name_split = sayer.split("-")
            sayers.writelines("define {} = Character ('{}', color=\"#AAAAAA\", who_outlines=[ (2, \"#000000\") ], what_outlines=[ (2, \"#000000\") ])\n".format(sayer_name_split[0],sayer_name_split[0]))
            continue        
        if " " in sayer:
            sayer_name_split = sayer.split(" ")
            sayers.writelines("define {} = Character ('{}', color=\"#AAAAAA\", who_outlines=[ (2, \"#000000\") ], what_outlines=[ (2, \"#000000\") ])\n".format(sayer_name_split[0],sayer_name_split[0]))
            continue        
        else:
            sayers.writelines("define {} = Character ('{}', color=\"#AAAAAA\", who_outlines=[ (2, \"#000000\") ], what_outlines=[ (2, \"#000000\") ])\n".format(sayer,sayer))
       

#number of ids approx 1090
'''
c=0
for i in json_data:
    c+=1
    print (json_data[c]["id"])
    print (json_data[c]["name"])

'''
'''
#list value of id 1
print (json_data[1]["list"])

for i in json_data[1]:
    print (i)
'''