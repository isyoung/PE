blue = 15
n = 21
limit = 1000000000000
while(n<limit):
	hold = 3*blue+2*n-2
	keep = 4*blue+3*n-3
	blue = hold
	n = keep

print(blue)