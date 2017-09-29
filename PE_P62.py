set = {}
for i in range(346, 10000):
    array = [x for x in str(i * i * i)]
    array.sort()
    _str = ''.join(array)
    if _str in set.keys():
        set[_str].append(i)
    else:
        set[_str] = [i]
    if len(set[_str]) == 5:
        print(int(set[_str][0]) ** 3)
        break