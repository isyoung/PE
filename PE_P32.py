from itertools import permutations

def get_permutations():
    result_set = set()
    permu_list = permutations('123456789', 9)
    for permu in permu_list:
        first_num = int(permu[0])
        second_num = int(permu[1]+permu[2]+permu[3]+permu[4])
        third_num = int(permu[5]+permu[6]+permu[7]+permu[8])
        if first_num*second_num == third_num:
            result_set.add(third_num)
        first_num = int(permu[0]+permu[1])
        second_num = int(permu[2]+permu[3]+permu[4])
        if first_num*second_num == third_num:
            result_set.add(third_num)
    return sum(result_set)

print(get_permutations())