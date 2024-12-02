data = [[int(y) for y in x.split(' ')] for x in open('input.txt').read().split('\n')]

######################
# Part 1
######################
def get_safety(numbers):
    delta = [int(numbers[i + 1]) - int(numbers[i]) for i in range(len(numbers) - 1)]
    # print(set(delta))
    if set(delta) <= {1,2,3} or set(delta) <= {-1, -2, -3}:
        return True
    return False

def safe_reports(data):
    return sum([get_safety(row) for row in data])

value = safe_reports(data)
print(value)

######################
# Part 2
######################
def safe_reports2(data):
    return sum([any([get_safety(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data])

value = safe_reports2(data)
print(value)