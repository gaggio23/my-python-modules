def count_lines_in_file(file):
	num_lines = sum(1 for line in open(file))
	file.close()
	return num_lines