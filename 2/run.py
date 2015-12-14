#!/usr/bin/python

import sys, logging

logger = logging.getLogger('scope.name')

logger.setLevel(logging.DEBUG)

stderr_log_handler = logging.StreamHandler()
stderr_log_handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(stderr_log_handler)

fh = logging.FileHandler('output')
fh.setLevel(logging.DEBUG)
fh.setFormatter( logging.Formatter('%(message)s') )
logger.addHandler(fh)


file = sys.stdin

total = 0

for line in file:

	dimensions = [int(x) for x in line.rstrip().split("x")]
	dimensions.sort()
	l, w, h = dimensions

	# normal area
	area = 2*l*w + 2*w*h + 2*h*l

	# Extra
	area += l*w

	total += area

	logger.info("total: %10s   new: %5s   dimensions: %12s   line: %10s", total, area, dimensions, line.rstrip())

print total

# 3697795
# 1448475
# 1585744