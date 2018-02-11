# coding: utf-8
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

import os
from os.path import join, exists

from landmark import detectLandmarks

def parse_args():
	"""Parse input arguments
	"""

	parser = ArgumentParser(description=__doc__,
							formatter_class=ArgumentDefaultsHelpFormatter)

	parser.add_argument('src',
						help='src')
	parser.add_argument('dst',
						help='dst')

	args = parser.parse_args()
	return args

if __name__ == '__main__':
    args = parse_args()
    # portal
    detectLandmarks(args.src, args.dst)
