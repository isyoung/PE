import csv
a = []
z = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(100):
	b = i*(i+1)/2
	a.append(b)
rdr = csv.reader(open("p042_words.csv"))
c = list(rdr)
for i in range(len(c[0])):
	if