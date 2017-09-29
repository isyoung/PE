import string
lets = {}
total_score = 0
f = open('names.txt')
for line in f:
 names = line.replace('"', '').lower().split(',')

names.sort()
a = 1
for e in string.lowercase:
 lets[e] = a
 a += 1

for i in range(0, names.__len__()):
 for e in names[i]:
  total_score += lets[e] * (i+1)

print (total_score)