import re
import os

cwd = os.getcwd()
#print(cwd)
test_line = "# | Story Telling only part"
line_with_or = test_line.split("|")
#print (line_with_or[1])
#print (":::",test_line[0])
file_name="voyeur.txt"
#file_name="test.txt"
file_name_without_ext=file_name.split(".")[0]

#f = open("{pwd}\\{fn}rpy.txt".format(fn=file_name_without_ext,pwd=cwd), "w")
f = open("{fn}_eng.txt".format(fn=file_name_without_ext),"w",encoding="utf-8")

line_num=1
with open(file_name, encoding="utf-8") as text_file:
    non_blank_lines = [line.strip() for line in text_file if line.strip()]
    for line in non_blank_lines:
        length_of_line = len(line)
        line=line.strip()
        #print (line)
        line = str(line).replace("'",'"')
        name_pattern =  r"[^A-Za-z0-9_ | \'^@#. <>\\//?=&!/-]+"
        eng_line = str(re.sub(name_pattern,'',line))
        print(eng_line)
        if "^" not in eng_line:
            f.writelines("\n {}\n".format(eng_line))
            continue
        if "^" in eng_line:
            f.writelines("     menuitem: {}\n".format(eng_line))
            continue