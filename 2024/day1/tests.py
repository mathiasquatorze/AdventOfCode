from challenge import get_distance, get_similarity_score

def test_get_distance():
    assert get_distance("example.txt") == 11

def test_get_similarity_score():
    assert get_similarity_score("example.txt") == 31