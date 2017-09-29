maxvalue = 1
with open('PE_P11_grid.txt') as file: array2d = [[int(digit) for digit in line.split()] for line in file]
for i in range(19):
	for p in range(16):
		a = array2d[i][p]*array2d[i][p+1]*array2d[i][p+2]*array2d[i][p+3]
		if maxvalue < a:
			maxvalue = a
for i in range(16):
	for p in range(19):
		b = array2d[i][p]*array2d[i+1][p]*array2d[i+2][p]*array2d[i+3][p]
		if maxvalue < b:
			maxvalue = b
for i in range(16):
	for p in range(3,16):
		c = array2d[i][p]*array2d[i+1][p+1]*array2d[i+2][p+2]*array2d[i+3][p+3]
		if maxvalue < c:
			maxvalue = c
for i in range(16):
	for p in reversed(range(3,16)):
		d = array2d[i][p]*array2d[i+1][p-1]*array2d[i+2][p-2]*array2d[i+3][p-3]
		if maxvalue < d:
			maxvalue = d
print(maxvalue)