#!/usr/bin/env python

#1
import argparse
parser = argparse.ArgumentParser( description="" )



parser.add_argument(
	"data_file",
	help="path to file we want to read",
)



#-------------------------------------------------------------------------------
# Are there other arguments we need?
#-------------------------------------------------------------------------------

args = parser.parse_args( )

#2
fh = open(args.data_file)

print("the file handle is", fh)

#3
lines = 0
words = 0
chars = 0

for line in fh:
	print(line)




#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
