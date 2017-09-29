f = open('PE_P13.txt', 'r')
l = [int(line) for line in f]
print(sum(l))