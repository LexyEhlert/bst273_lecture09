#!/usr/bin/env python

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

# how do we see if this actually works?

print(args)
print(args.data_file)

#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
