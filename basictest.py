import glob 
import sys
import os.path
import pandas as pd
import modul as m

result=[]
new_server=[]
new_tgt_file=[]

def test_target_files(target_file_list,unique_server_names):
    print("TestCase1: This testcase checks whether the names of distinct servernames present in input csv file is same as the output file names")
    print("Example: If distinct of servernames (a field in input csv file) is asia_server and Australia_server, then output files should be named as asia_server.txt and Austraia_server.txt respectively.")
    target_file_list.sort()
    unique_server_names.sort()
    
    for j in target_file_list:
        p=os.path.basename(os.path.normpath(j))
        new_tgt_file.append(p)
    for i in unique_server_names:
        new_server_name=str(i)+".txt"
        new_server.append(new_server_name)

    if new_tgt_file == new_server:
        print("Target Files created are: "+str(new_tgt_file))
        print("Unique Server names from input csv file is: "+str(new_server))
        print("Both are equal and hence this testcase is passed")
        print("--------------------------------------------------------")
    else:
        print("Target Files created are: "+str(new_tgt_file))
        print("Unique Server names from input csv file is: "+str(new_server))
        print("Both are unequal and hence this testcase is Failed")
        print("--------------------------------------------------------")
def test_count_of_lines(path,unique_server_names,data1,d2,d3):

    print("TestCase2: This testcase counts the lines for each servername in all the input csv file and checks the count against the records inserted in each target files")
    print("Example: If there are 3 records for asia_server (servername) in one input csv file, and there are 5 such input files, then totally asia_server records will sum upto 15 (3 recs*5 files)")
    print("Sae15 records should be present in asia_server.txt output file. Lets Check")

    cnt=0
    unique_server_names.sort()
    for i in unique_server_names:
        num_lines=0
        fil=str(path)+str(i)+".txt"
        with open(fil,'r') as fil:
            for line in fil:
                if i in line:
                    num_lines += 1                    
        if int(num_lines) == int(data1):
            print("Number of Records for servername: "+str(i)+" in all the source files is "+str(data1))
            print("Number of lines for servername : "+str(i)+" in the output file "+str(i)+".txt file is "+str(num_lines))
            print("Number of records matches between source and target files, for "+str(i)+" server data")
            print("--------------------------------------------------------")
            result.append("Y")
        elif int(num_lines) == int(d2):
            print("Number of Records for servername: "+str(i)+" in all the source files is "+str(data1))
            print("Number of lines for servername : "+str(i)+" in the output file "+str(i)+".txt file is "+str(num_lines))
            print("Number of records matches between source and target files, for "+str(i)+" server data")
            print("--------------------------------------------------------")
            result.append("Y")
        elif int(num_lines) == int(d3):
            print("Number of Records for servername: "+str(i)+" in all the source files is "+str(data1))
            print("Number of lines for servername : "+str(i)+" in the output file "+str(i)+".txt file is "+str(num_lines))
            print("Number of records matches between source and target files, for "+str(i)+" server data")
            print("--------------------------------------------------------")
            result.append("Y")
        else:
            print("Number of lines do not match between source and target files for "+str(i)+" server data")
            result.append("N")

        if "N" in result:
            print("Testcase for line count check failed")
			
        else:
            print("Testcase for line count check Passed")            
        

			
			
		        