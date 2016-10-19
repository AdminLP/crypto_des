from utils import int2bin
from initial_data import input1
from calculations import input2, output1_S1, output2_S1, deltaC_S1, \
    output1_S2, output2_S2, deltaC_S2, \
    output1_S3, output2_S3, deltaC_S3, \
    probability_S1, probability_S2, probability_S3


def beautiful_output_in_the_console(input1, input2, output1, output2, deltaC):
    for i in range(16):
        print('Таблица №' + str(i + 1))
        print('-' * 74)
        print('|' + 'Вход_1' + '\t | \t' + 'Вход_2' + '\t | \t' +
              'Выход_1' + '\t | \t' + 'Выход_2' + '\t | \t' +
              'Дельта_C' + ' |')
        print('-' * 74)
        for j in range(16):
            print('|' + int2bin(input1[j]) + '\t | \t' +
                  int2bin(input2[i][j]) + '\t | \t' +
                  int2bin(output1[j]) + '\t | \t' +
                  int2bin(output2[i][j]) + '\t | \t' +
                  int2bin(deltaC[i][j]) + '\t |')
        print('-' * 74)
        print('\n')


def output_probability_in_the_console(probability_list, j, k):
    print('dA\dC\t' + '|' + '\t'.join(int2bin(n, j) for n in range(k)))
    print('-' * 66)
    for i in range(16):
        print(int2bin(i) + '\t' + '|' + '\t'.join(str(n) for n in [probability_list[i].get(j, 0) for j in range(k)]))
    print('\n')


def main_output_console():
    print('S1 Table')
    beautiful_output_in_the_console(input1, input2, output1_S1, output2_S1, deltaC_S1)
    print('S2 Table')
    beautiful_output_in_the_console(input1, input2, output1_S2, output2_S2, deltaC_S2)
    print('S3 Table')
    beautiful_output_in_the_console(input1, input2, output1_S3, output2_S3, deltaC_S3)
    print('Probability S1 Table')
    output_probability_in_the_console(probability_S1, 3, 8)
    print('Probability S2 Table')
    output_probability_in_the_console(probability_S2, 3, 8)
    print('Probability S3 Table')
    output_probability_in_the_console(probability_S3, 2, 4)
