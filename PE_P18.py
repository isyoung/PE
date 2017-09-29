with open('PE_P18_triangle.txt') as file: 
	ta2d = [[int(digit) for digit in line.split()] for line in file]
for i in reversed(range(1,len(ta2d))):
	for j in range(len(ta2d[i])-1):
		ta2d[i-1][j] += max(ta2d[i][j],ta2d[i][j+1])
print(ta2d[0][0])