from operator import xor
from utils import int2bin
from initial_data import input1, deltaA, S1, S2, S3


def calculate_input2(input1, deltaA):
    return [[xor(input1[j], deltaA[i]) for j in input1] for i in deltaA]


def output_calculation_after_table_2x8(input, table):
    return [table[int(int2bin(input[i])[0])][int(int2bin(input[i])[1:], 2)] for i in range(16)]


def output_calculation_after_table_4x4(input, table):
    return [table[int((int2bin(input1[i])[0] + int2bin(input1[i])[-1]), 2)][int(int2bin(input[i])[1:-1], 2)] for i in range(16)]


def calculate_delta_c(output1, output2):
    return [[xor(output1[j], output2[i][j]) for j in range(16)] for i in range(16)]


def probability(deltaC):
    the_number_of_occurrences = [{} for i in range(16)]
    for i in range(16):
        for n in deltaC[i]:
            if n in the_number_of_occurrences[i].keys():
                the_number_of_occurrences[i][n] += 1
            else:
                the_number_of_occurrences[i][n] = 1
    return the_number_of_occurrences

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
