import re
import os
import json

common_file_name="CommonEvents.json"
#movies_file_name="CommonEvents.json"

common_json_file=open(common_file_name)
movies_file_name = open("movies.rpy","w",encoding="utf-8")
common_json_data = json.load(common_json_file)


print ("common_id::",common_json_data[664]["name"])

for x in range(1,131):
    file_name = "Map{}.json".format(f'{x:03}')

    print (file_name)
    #file_name="Map019.json"

    json_file=open(file_name,encoding="utf8")
    json_data = json.load(json_file)
    file_name_without_ext=file_name.split(".")[0]
    
    count = 0
    current_char = ""
    prev_dialogue = ""
    sayer_list = []
    menu_name = []
    menu_name0 = ""
    menu_name1 = ""
    menu_name2 = ""
    menu_name3 = ""
    menu_name4 = ""
    menu_name5 = ""
    prev_dialogue = ""

    print (json_data["parallaxName"])

    #map_name = json_data["parallaxName"]

    num_pattern =  r'[^0-9]+'
    map_num = str(re.sub(num_pattern,'',file_name_without_ext))
    map_num = int(map_num.lstrip('0'))

    print ("map_num::",map_num)


    map_file = open("Mapinfos.json")
    json_map = json.load(map_file)
    #print (json_map[map_num]["name"])
    map_name = json_map[map_num]["name"].replace(" ", "_")
    name_pattern =  r'[^A-Za-z0-9_]+'
    map_name = str(re.sub(name_pattern,'',map_name))
    print (map_name)

    f = open("{fn}.rpy".format(fn=map_name),"w",encoding="utf-8")
    sayers = open("sayer.rpy","w",encoding="utf-8")

    count = 0
    for i in json_data["events"]:
        count+=1
        #print (json_data["events"][])
        try:
            for json_list in json_data["events"][count]["pages"]:
                #print (json_list["list"])
                #print (json_list["list"][count]["parameters"])
                label_with_underscore = json_data["events"][count]["name"].replace(" ","")
                note_with_underscore = json_data["events"][count]["note"].replace(" ","_")
                if (count == 1):
                    pattern = r'[^A-Za-z0-9_]+'
                    label_without_special_char = re.sub(pattern, '', label_with_underscore)
                    mote_without_special_char = re.sub(pattern, '', note_with_underscore)
                    f.writelines('  \nlabel {}:\n'.format(label_without_special_char+mote_without_special_char+"_"+map_name))
                if (label_with_underscore == "Timeofday"):
                    first_label = str(file_name_without_ext)
                    print(first_label)
                    f.writelines('  \nlabel {}:\n'.format(first_label))
                else:
                    pattern = r'[^A-Za-z0-9_]+'
                    label_without_special_char = re.sub(pattern, '', label_with_underscore)
                    mote_without_special_char = re.sub(pattern, '', note_with_underscore)
                    if (count != 1):
                        f.writelines('  return\n\nlabel {}:\n'.format(label_without_special_char+mote_without_special_char+"_"+map_name))
                for per_list in json_list["list"]:
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
                                pattern = r'[^A-Za-z0-9_ ]+'
                                menu_items = re.sub(pattern, '', menu_items)
                                f.writelines('    \"{}\":\n'.format(menu_items))
                                jump_with_underscore = str(menu_items).replace(" ","_")
                                pattern = r'[^A-Za-z0-9_]+'
                                jump_without_special_char = re.sub(pattern, '', jump_with_underscore)
                                f.writelines('      call {}\n'.format(jump_without_special_char))
                    if (str(len(per_list["parameters"])) == "2"):
                        #print (menu_name)  
                        #print(per_list["parameters"][1])
                        #if (str(per_list["parameters"][1]) == str(menu_name[0]) or str(per_list["parameters"][1]) == str(menu_name[1])):
                        if (per_list["parameters"][1] == menu_name0 or per_list["parameters"][1] == menu_name1 or per_list["parameters"][1] == menu_name2 or per_list["parameters"][1] == menu_name3 or per_list["parameters"][1] == menu_name4 or per_list["parameters"][1] == menu_name5):
                            #print (per_list["parameters"][1])
                            label_with_underscore = str(per_list["parameters"][1]).replace(" ","_")
                            pattern = r'[^A-Za-z0-9_]+'
                            label_without_special_char = re.sub(pattern, '', label_with_underscore)
                            f.writelines('label {}:\n'.format(label_without_special_char))
                            continue
                        else:
                            print (per_list["parameters"][1])
                            #print ("m1",menu_name1)
                            #print ("m2",menu_name2)
                    if (str(len(per_list["parameters"])) == "1" and str(per_list["parameters"][0]).isdigit()):
                        common_label_with_underscore = common_json_data[per_list["parameters"][0]]["name"]
                        pattern = r'[^A-Za-z0-9_]+'
                        common_label_without_special_char = re.sub(pattern, '', common_label_with_underscore)
                        #f.writelines('\nlabel {}:\n'.format(common_label_without_special_char+"_"+"CommonEvents"))
                        if (common_label_without_special_char != "Timeofday"):
                            f.writelines('  call {}\n'.format(common_label_without_special_char+"_"+"CommonEvents"))
                    if (str(len(per_list["parameters"])) == "1" and "Lbl" in str(per_list["parameters"][0]) and "LblEnd" not in str(per_list["parameters"][0]) and "LblContinue" not in str(per_list["parameters"][0])):
                        #print (per_list["parameters"][0])
                        print ("")
                    if (str(len(per_list["parameters"])) == "1" or str(len(per_list["parameters"])) == "4"):
                        if (str(len(per_list["parameters"])) == "1" and not str(per_list["parameters"][0]).isdigit() and per_list["parameters"][0] != "" and ".webm" in per_list["parameters"][0]):
                            print (per_list["parameters"][0])
                            #movies_file_name.writelines(per_list["parameters"][0])
                        if (str(len(per_list["parameters"])) == "4" and not str(per_list["parameters"][0]).isdigit()):
                            #print (":::",per_list["parameters"][0])
                                current_char = per_list["parameters"][0]

                                if current_char not in sayer_list:
                                    sayer_list.append(current_char)
                        if (str(len(per_list["parameters"])) == "1" and not str(per_list["parameters"][0]).isdigit() and per_list["parameters"][0] != "" and ".webm" not in per_list["parameters"][0]):
                            #print (":::",per_list["parameters"][0])
                            if (prev_dialogue != per_list["parameters"][0] and "{" not in str(per_list["parameters"][0])):
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
                                        #print(current_char_split[0])
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
                        #if "GwynnethandInnkeeper" in per_list["parameters"][0]: 
                        #    print(per_list["parameters"])
                        if ( per_list["parameters"][1] != "" and not str(per_list["parameters"][1]).isdigit()):
                            lower_of_scene = per_list["parameters"][1].lower()
                            lower_of_scene = lower_of_scene.replace(" ","_")
                            lower_of_scene = lower_of_scene.replace("'","_")
                            if "missing" not in lower_of_scene:
                                f.writelines("  scene {} \n".format(lower_of_scene))            
        except:
            print("exception")    
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
    

    #use id 256 for testing which has images
    count = 0
    current_char = ""
    prev_dialogue = ""
    sayer_list = []
    