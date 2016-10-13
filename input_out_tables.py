from operator import xor

input1 = [x for x in range(16)]
deltaA = [x for x in range(16)]
S1 = [[1, 6, 2, 1, 5, 0, 7, 2], [4, 5, 6, 3, 4, 7, 3, 0]]


def int2bin(n, count=4):
    return "".join([str((n >> y) & 1) for y in range(count - 1, -1, -1)])


def calculate_input2(input1, deltaA):
    return [[xor(input1[j], deltaA[i]) for j in input1] for i in deltaA]

input2 = calculate_input2(input1, deltaA)


def output_calculation_after_table_s1(input, table):
    return [table[int(int2bin(input[i])[0])][int(int2bin(input[i])[1:], 2)] for i in range(16)]


def calculate_delta_c(output1, output2):
    return [[xor(output1[j], output2[i][j]) for j in range(16)] for i in range(16)]

output1 = output_calculation_after_table_s1(input1, S1)
output2 = [output_calculation_after_table_s1(input2[i], S1) for i in range(16)]
deltaC = calculate_delta_c(output1, output2)
# print(output1)
# print(output2)


def beautiful_output_in_the_console(input1, input2):
    for i in range(16):
        print('Таблица №' + str(i+1))
        print('-' * 74)
        print('|' + 'Вход_1' + '\t | \t' + 'Вход_2' + '\t | \t' +
              'Выход_1' + '\t | \t' + 'Выход_2' + '\t | \t' +
              'Дельта_C' + ' |')
        print('-'*74)
        for j in range(16):
            print('|' + int2bin(input1[j]) + '\t | \t' +
                  int2bin(input2[i][j]) + '\t | \t' +
                  int2bin(output1[j]) + '\t | \t' +
                  int2bin(output2[i][j]) + '\t | \t' +
                  int2bin(deltaC[i][j]) + '\t |')
        print('-' * 74)
        print('\n')

beautiful_output_in_the_console(input1, input2)

