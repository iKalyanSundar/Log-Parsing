import glob
import sys
import os.path
import pandas as pd

#function to get path in which csv files should be scanned
def get_file_path_input():
    input_path=input("Enter Path where the output file has to be created: ")
    while (input_path is None) or (input_path == ''):
        input_path=input("Enter Path where the output file has to be created: ")
    if os.path.exists(input_path):
        return input_path
    else:
        os.mkdir(input_path)
        return input_path

#Function to get number of input files to be generated, from user		
def get_num_of_input_files():
    num_file=input("Enter number of input csv files that neeeds to be generated: ")
    while(num_file is None or num_file == ''):
        num_file=input("Enter number of input csv files that neeeds to be generated: ")
    return num_file

#Function to get number of sets of 3 line string to be written to each input csv file
def get_num_of_lines():
    num_lines=input("Enter number of sets of 3 line input string to be generated in each input csv files: ")
    while(num_lines is None or num_lines == ''):
        num_file=input("Enter number of input csv files that neeeds to be generated: ")
    return num_lines
	
#function to check if a filepath exists or not (returns true or false)
def path_check(pathofFile):
    path_chk=os.path.exists(pathofFile)
    return path_chk
	
#function to create dataframe from csv file
def create_df(filepath,nm):
    if (filepath is None or nm is None) or (filepath == '' or nm == ''):
        print("Both filepath and header list are mandatory parameter for creating a dataframe. Please provide all parameters")
	    #creating an empty dataframe
        data=pd.DataFrame()
        return data		
    else:
        data=pd.read_csv(filepath,names=nm)
        return data
        
#function to remove specified extension files from the specified path
def remove_files_from_dir(path,ext):
    full_ext="."+str(ext)
    filelist = [ f for f in os.listdir(str(path)) if f.endswith(full_ext) ]
    for f in filelist:
        os.remove(os.path.join(str(path),f))
        
	
