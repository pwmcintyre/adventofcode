#!/usr/bin/python

import sys, logging

logger = logging.getLogger('scope.name')

logger.setLevel(logging.DEBUG)

stderr_log_handler = logging.StreamHandler()
logger.addHandler(stderr_log_handler)

# nice output format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stderr_log_handler.setFormatter(formatter)

logger.info('Info message')
logger.error('Error message')

file = sys.stdin
floor = 0
move = 0

for line in file:

	for c in line:

		move += 1

		go = 1 if c is '(' else -1 if c is ')' else 0

		floor += go
		logger.info("floor: %5s char: %s direction: %2s move: %5s", floor, c, go, move)

		if floor < 0:
			break
