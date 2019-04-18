#Author: topvl.net 
from os import listdir
from os.path import isfile, join
import os
import sys
import platform
import subprocess
import time
import array as arr


import argparse

text = "===================\nSplit File to 2 files (by a rate)\n===================="

parser = argparse.ArgumentParser(description = text)  
#parser.parse_args()  

jobIds = arr.array('i')

parser.add_argument("-f", "--filex", help="The file need split")
parser.add_argument("-r", "--ratex", help="the rate to split")
parser.add_argument("-o", "--output", help="the output folder")

# read arguments from the command line
args = parser.parse_args()

if args.filex:
	filex = args.filex
else:
	filex = "data.dat"

if args.ratex:
	ratex = float(args.ratex)
else:
	ratex = 0.1
	
if args.output:
	output = args.output
else:
	output = "OutputFolder"


def createFolder(folder):
	if not os.path.isdir(folder):
		cmd = 'mkdir '+folder
		os.system(cmd)
	else:
		#cmd = 'rm -rf '+folder
		#os.system(cmd)
		#os.system('mkdir '+folder)
		print(folder+"'s exists.")

def getLines(files):
	with open(files) as f:
		return sum(1 for _ in f)
		
createFolder(output)


#files = [f for f in listdir(folder) if isfile(join(folder, f))]				

#for f in files:
#	if "-" in f:
#		f1 = str(f).replace("-","_")
#		os.system('mv '+folder+'/'+str(f)+' '+folder+'/'+f1)
i = 0
infile = open(filex,'r')
filename = filex.split("/")[len(filex.split("/"))-1]
#first_line = infile.readline()
#seq = first_line.split(" ")
seq = getLines(filex)

if(os.path.isfile(output+"/"+filename+"_1")):
	os.system('rm '+output+"/"+filename+"_1")


if(os.path.isfile(output+"/"+filename+"_2")):
	os.system('rm '+output+"/"+filename+"_2")

first_file = open(output+"/"+filename+"_1","w+")
second_file = open(output+"/"+filename+"_2","w+")

first_number = int(round(int(seq)*ratex))
#first_file.write(str(first_number)+" "+str(seq[1]))

second_number = int(seq)-int(round(int(seq)*ratex))
#second_file.write(str(second_number)+" "+str(seq[1]))

for line in infile:
	if(i < first_number):
		first_file.write(line)
	else:
		second_file.write(line)
	i=i+1
infile.close()
first_file.close()
second_file.close()
	
#print("Splitted File: "+filex+" splitted rate:"+str(ratex)+" Total lines:"+str(seq[0])+" taxa:"+str(seq[1]))