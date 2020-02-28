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

text = "===================\nSplit wildcard-files in a folder (by a rate)\n===================="

parser = argparse.ArgumentParser(description = text)  
#parser.parse_args()  

jobIds = arr.array('i')

parser.add_argument("-d", "--directory", help="directory")
parser.add_argument("-w", "--wildcard", help="wirdcard")
parser.add_argument("-r", "--ratex", help="the rate to split")
parser.add_argument("-o", "--output", help="the output folder")

# read arguments from the command line
args = parser.parse_args()

folder = args.directory

if args.wildcard:
	wildcard = args.wildcard
else:
	wildcard = "data"

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
		
createFolder(output)

files = [f for f in listdir(folder) if isfile(join(folder, f))]				

for f in files:
	if wildcard in f:
		os.system('python splitFile.py -f '+folder+'/'+f+' -r '+str(ratex)+' -o '+output)
		print('Process file '+f+' completed. \n')

#for f in files:
#	if "-" in f:
#		f1 = str(f).replace("-","_")
#		os.system('mv '+folder+'/'+str(f)+' '+folder+'/'+f1)
