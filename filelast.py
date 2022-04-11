def read_lastnlines(fname,n):
	with open('sample.txt') as f:
		for line in (f.readlines() [-n:]):
			print(line)

read_lastnlines('sample.txt',3)