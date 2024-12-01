def lists(filename):
    left = []
    right = []
    with open(filename) as file:
        for line in file:
            left_value, right_value = map(int, line.split())
            left.append(left_value)
            right.append(right_value)

    left.sort()
    right.sort()
    
    distance = sum(abs(a - b) for a, b in zip(left, right))
    print(distance)
    return distance

distance = lists("input.txt")
print("Distance: " + str(distance))