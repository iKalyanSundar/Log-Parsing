import glob 
import sys
import os.path
import pandas as pd
import modul as m
import basictest as u

print("Program starts")

whole_data_s1=0
whole_data_s2=0
whole_data_s3=0

#Function call to get the path where the output files has to be placed/created
path=m.get_file_path_input()

#Function call to remove existing output files(if any) from the path provided
m.remove_files_from_dir(path,'txt')

#Getting all csv files from the provided path
csv_file_list1=glob.glob(path+"*.csv")
print(csv_file_list1)
csv_file_list=csv_file_list1

#loop through each file
for f in csv_file_list1:
    print("Loop")
    
    #Forming dataframe out of the input csv file received from csv_file_list
    data=m.create_df(f,['timestamp','servername','applicationName','productName','comments'])
    
    #Getting unique servername from dataframe
    unique=data['servername'].unique()
    
    #Getting count of records for each servername in source file
    server_line_count_s1=data[data['servername'] == 'server1']
    server_line_count_s2=data[data['servername'] == 'server2']
    server_line_count_s3=data[data['servername'] == 'server3']
    
    whole_data_s1=whole_data_s1+len(server_line_count_s1.index)
    whole_data_s2=whole_data_s2+len(server_line_count_s2.index)	
    whole_data_s3=whole_data_s3+len(server_line_count_s3.index)	
	
	#Looping through the unique servernames
    for i in unique:
        fname=str(i)+'.txt'
        filepath=str(path)+str(fname)
        csvpath=str(path)+str(i)+".csv"
        
        #Checking if the target file exists in the path - Function call is made for that
        a=m.path_check(filepath)
        if a:
            #opening the target file in append mode
            f=open(filepath,'a')
            val=data[data['servername']==i]
			
            #Writing dataframe data(excluding header) into an intermediate csv file
            val.to_csv(csvpath,header=False,index=False)
            data_without_hdr=pd.read_csv(csvpath)
  
            #Writing dataframe data to output file
            with pd.option_context('display.max_rows',None,'display.max_columns',None):
                print("Writing to file....")
                f.write(str(data_without_hdr)+'\n')
            #Remove the intermediate csv file
            os.remove(csvpath)
        else:
            #opening the target file in write mode
            f=open(filepath,'w')
            val=data[data['servername']==i]
			
            #Writing dataframe data(excluding header) into an intermediate csv file
            val.to_csv(csvpath,header=False,index=False)
            data_without_hdr=pd.read_csv(csvpath)
  
            #Writing dataframe data to output file
            with pd.option_context('display.max_rows',None,'display.max_columns',None):
                print("Writing to file....")
                f.write(str(data_without_hdr)+'\n')
            #Remove the intermediate csv file
            os.remove(csvpath)
			
        f.close()

testing=input("Proceed with Unit testing results ?? ")
while testing is None or testing == '':
    testing=input("Proceed with Unit testing results ?? ")    
if testing == 'Y' or testing == 'y':
    if "win" in sys.platform:
        tgt_file_list = glob.glob(str(path)+"*.txt")
        u.test_target_files(tgt_file_list,unique)
        u.test_count_of_lines(str(path),unique,whole_data_s1,whole_data_s2,whole_data_s3)
    else:
        tgt_file_list = glob.glob(str(path)+"*.txt")
        u.test_target_files(tgt_file_list,unique)
        u.test_count_of_lines(unique,whole_data_s1,whole_data_s2,whole_data_s3)
		
else:
    print("Unit testing option is not opted. Y or y should be provided by the user inorder to execute and give the unit testing results. Please try again executing this script from the beginning")
    
print("Program Ends")	