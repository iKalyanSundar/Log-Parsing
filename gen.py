import os
import pandas as pd
import time
import modul as m

print("Program starts")
print("This feature will create the necessary input csv files in a particular path provided by the user")

str1='01/01/2019 00:00:00,server1,application1,product1,comment1'
str2='01/01/2019 00:00:00,server2,application1,product1,comment1'
str3='01/01/2019 00:00:00,server3,application1,product1,comment1'

pth=m.get_file_path_input()
num_ip_file=m.get_num_of_input_files()
num_lines_per_file=m.get_num_of_lines()

print("The 3 line string that will be written to input csv file for "+str(num_lines_per_file)+" is ")
print(str1)
print(str2)
print(str3)

#Removing existing csv input files present in the path
m.remove_files_from_dir(str(pth),"csv")

for j in range(0,int(num_ip_file)):
    if os.path.exists(str(pth)+"kal"+str(j)+".csv"):
        f=open(str(pth)+"kal"+str(j)+".csv",'w')
    else:
        f=open(str(pth)+"kal"+str(j)+".csv",'w')        
		
    for i in range(0,int(num_lines_per_file)):
        f.write(str(str1)+'\n')
        f.write(str(str2)+'\n')
        f.write(str(str3)+'\n')
		
print("Program Ends")
