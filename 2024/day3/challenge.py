import re

with open('input.txt', 'r') as file:
    data = file.read().replace('\n', '')

with open('example.txt', 'r') as file:
    example_data = file.read().replace('\n', '')

with open('example2.txt', 'r') as file:
    example_data2 = file.read().replace('\n', '')

def get_mul_instances(input):
    return input.split("mul")

def get_mul_result(mul):
    pattern = r'\(\d{1,3},\d{1,3}\)'
    if re.search(pattern, mul):
        halves = mul.split(",")
        first_half = int(halves[0].split("(")[1])
        second_half = int(halves[1].split(")")[0])
        return first_half*second_half
    else:
        return 0

###############
# Part 1
###############
def get_sum_mul(string):
    result = 0
    mul_instances = get_mul_instances(string)
    for mul in mul_instances:
        result += get_mul_result(mul[0:9])
    return result

value = get_sum_mul(example_data)
print(value)

###############
# Part 2
###############
def get_sum_mul_conditional(input):
    result = 0
    split_by_dont = input.split("don't()")
    for i in range(len(split_by_dont)):
        if i == 0:
            result += get_sum_mul(split_by_dont[i])
        else:
            split_by_do = split_by_dont[i].split("do()")
            for i in range(len(split_by_do)):
                if i > 0:
                    result += get_sum_mul(split_by_do[i])
            
    return result

value = get_sum_mul_conditional(data)
print(value)