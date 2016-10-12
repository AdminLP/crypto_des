from operator import xor

input1 = [x for x in range(16)]
deltaA = [x for x in range(16)]


def int2bin(n, count=4):
    return "".join([str((n >> y) & 1) for y in range(count - 1, -1, -1)])


def calculate_input2(input1, deltaA):
    return [[xor(input1[j], deltaA[i]) for j in input1] for i in deltaA]

input2 = calculate_input2(input1, deltaA)


def beautiful_output_in_the_console(input1, input2):
    for i in range(16):
        print('Вход_1' + '\t\t' + 'Вход_2' + '\t\t' + 'Выход_1' + '\t\t' + 'Выход_2' + '\t\t' + 'дельта_C')
        for j in range(16):
            print(int2bin(input1[j]) + '\t\t' + int2bin(input2[i][j]))
        print('\n')

beautiful_output_in_the_console(input1, input2)

