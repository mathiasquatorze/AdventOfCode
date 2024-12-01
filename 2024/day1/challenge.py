##############################################
# Part 1
##############################################
def get_distance(filename):
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

distance = get_distance("input.txt")
print("Distance: " + str(distance))

##############################################
# Part 2
##############################################
def get_similarity_score(filename):
    left = []
    right = []
    with open(filename) as file:
        for line in file:
            left_value, right_value = map(int, line.split())
            left.append(left_value)
            right.append(right_value)
    scores = []
    for i in left:
        similarity_count = 0
        for j in right:
            if i == j:
                similarity_count += 1
        score = i*similarity_count
        scores.append(score)

    return sum(scores)

score = get_similarity_score("input.txt")
print(score)