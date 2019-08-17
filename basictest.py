import glob 
import sys
import os.path
import pandas as pd
import modul as m

result=[]
new_server=[]
new_tgt_file=[]

def test_target_files(target_file_list,unique_server_names):
    print("==========================================================TESTCASE 1================================================================\n")
    print("TestCase1: \n This testcase checks whether the filenames of output files that are generated are same as,\n names of distinct values in the field servernames of input csv files, concatenated with .txt as extension\n")
    print("-------------------------------------------------------------------------------------\n")
    print("Example: \n If distinct of servernames (a field in input csv file) is asia_server and Australia_server,\n then output files should be named as asia_server.txt and Austraia_server.txt respectively.\n")
    print("-------------------------------------------------------------------------------------\n")    
    target_file_list.sort()
    unique_server_names.sort()
    
    for j in target_file_list:
        p=os.path.basename(os.path.normpath(j))
        new_tgt_file.append(p)
    for i in unique_server_names:
        new_server_name=str(i)+".txt"
        new_server.append(new_server_name)

    if new_tgt_file == new_server:
        print("Output files generated are: "+str(new_tgt_file))
        print("Distinct values from the field, servernames, from the input csv files are: "+str(new_server))
        print("Names of output files generated and Distinct values in the field servernames from input csv files are matching and hence test case 1 is passed\n")
        result.append("Y")
    else:
        print("Output files generated are: "+str(new_tgt_file))
        print("Distinct values from the field, servernames, from the input csv files are: "+str(new_server))
        print("Names of output files generated and Distinct values in the field servernames from input csv files are matching and hence test case 1 is failed\n")
        result.append("Y")
		
    if "N" in result:
        print("Testcase 1 failed\n")
        print("=====================================================TESTCASE 2===========================================================\n")
    else:
        print("Testcase 1 passed\n")   
        print("=====================================================TESTCASE 2===========================================================\n")
		
def test_count_of_lines(unique_server_names,data,file_path):
    idx=0

    print("TestCase2:\n This testcase counts the lines for each servername in all the input csv file\n and checks the count against the records inserted in each target files\n")
    print("-------------------------------------------------------------------------------------\n")
    print("Example:\n If there are 3 records for asia_server (servername) in one input csv file,\n and there are 5 such input files, then totally asia_server records will sum upto 15 (3 recs*5 files)\n")
    print("Same 15 records should be present in asia_server.txt output file. Lets Check\n")
    print("-------------------------------------------------------------------------------------\n")	

    cnt=0
    unique_server_names.sort()
    for i in unique_server_names:
        num_lines=0
        fil=str(file_path)+str(i)+".txt"
        with open(fil,'r') as fil:
            for line in fil:
                if i in line:
                    num_lines += 1                    
        if int(num_lines) == int(data[idx]):
            print("Number of Records for servername: "+str(i)+" in all the source files is "+str(data[idx]))
            print("Number of lines for servername : "+str(i)+" in the output file "+str(i)+".txt file is "+str(num_lines))
            print("Number of records matches between source and target files, for "+str(i)+" server data")
            print("--------------------------------------------------------")
            result.append("Y")
        else:
            print("Number of lines do not match between source and target files for "+str(i)+" server data")
            result.append("N")
			
        idx=idx+1

    if "N" in result:
        print("Testcase 2 failed")
    else:
        print("Testcase 2 Passed")            
        

			
			
		        