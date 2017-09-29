total = 0
for i in range(2,229999):
    c = sum([int(x)**5 for x in str(i)])
    if c == i:
        total += i
print(total)