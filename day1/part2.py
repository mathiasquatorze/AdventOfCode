def similarity_score(filename):
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

example_similarity_score = similarity_score("example.txt")
print(example_similarity_score)

similarity_score = similarity_score("input.txt")
print(similarity_score)