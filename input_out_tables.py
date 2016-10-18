from operator import xor

input1 = [x for x in range(16)]
deltaA = [x for x in range(16)]
S1 = [[1, 6, 2, 1, 5, 0, 7, 2], [4, 5, 6, 3, 4, 7, 3, 0]]
S2 = [[1, 3, 0, 2, 3, 5, 6, 2], [7, 4, 5, 1, 4, 6, 0, 7]]
S3 = [[2, 2, 0, 0], [1, 0, 0, 2], [2, 1, 3, 3], [1, 1, 3, 3]]


def int2bin(n, count=4):
    return "".join([str((n >> y) & 1) for y in range(count - 1, -1, -1)])


def calculate_input2(input1, deltaA):
    return [[xor(input1[j], deltaA[i]) for j in input1] for i in deltaA]


def output_calculation_after_table_2x8(input, table):
    return [table[int(int2bin(input[i])[0])][int(int2bin(input[i])[1:], 2)] for i in range(16)]


def output_calculation_after_table_4x4(input, table):
    return [table[int((int2bin(input1[i])[0] + int2bin(input1[i])[-1]), 2)][int(int2bin(input[i])[1:-1], 2)] for i in range(16)]


def calculate_delta_c(output1, output2):
    return [[xor(output1[j], output2[i][j]) for j in range(16)] for i in range(16)]


def beautiful_output_in_the_console(input1, input2, output1, output2, deltaC):
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


def probability(deltaC):
    the_number_of_occurrences = [{} for i in range(16)]
    for i in range(16):
        for n in deltaC[i]:
            if n in the_number_of_occurrences[i].keys():
                the_number_of_occurrences[i][n] += 1
            else:
                the_number_of_occurrences[i][n] = 1
    return the_number_of_occurrences


def output_probability_in_the_console(probability_list):
    print('dA\dC\t' + '|' + '\t'.join(int2bin(n, 3) for n in range(8)))
    print('-' * 66)
    for i in range(16):
        print(int2bin(i) + '\t' + '|' + '\t'.join(str(n) for n in [probability_list[i].get(j, 0) for j in range(8)]))
    print('\n')


def main_output_console():
    print('S1 Table')
    beautiful_output_in_the_console(input1, input2, output1_S1, output2_S1, deltaC_S1)
    print('S2 Table')
    beautiful_output_in_the_console(input1, input2, output1_S2, output2_S2, deltaC_S2)
    print('S3 Table')
    beautiful_output_in_the_console(input1, input2, output1_S3, output2_S3, deltaC_S3)
    print('Probability S1 Table')
    output_probability_in_the_console(probability_S1)
    print('Probability S2 Table')
    output_probability_in_the_console(probability_S2)
    print('Probability S3 Table')
    output_probability_in_the_console(probability_S3)

input2 = calculate_input2(input1, deltaA)
output1_S1 = output_calculation_after_table_2x8(input1, S1)
output2_S1 = [output_calculation_after_table_2x8(input2[i], S1) for i in range(16)]
deltaC_S1 = calculate_delta_c(output1_S1, output2_S1)

output1_S2 = output_calculation_after_table_2x8(input1, S2)
output2_S2 = [output_calculation_after_table_2x8(input2[i], S2) for i in range(16)]
deltaC_S2 = calculate_delta_c(output1_S2, output2_S2)

output1_S3 = output_calculation_after_table_4x4(input1, S3)
output2_S3 = [output_calculation_after_table_4x4(input2[i], S3) for i in range(16)]
deltaC_S3 = calculate_delta_c(output1_S3, output2_S3)
probability_S1 = probability(deltaC_S1)
probability_S2 = probability(deltaC_S2)
probability_S3 = probability(deltaC_S3)


main_output_console()