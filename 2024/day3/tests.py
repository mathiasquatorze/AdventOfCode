from challenge import example_data, example_data2, data, get_sum_mul, get_mul_result, get_sum_mul_conditional

def test_get_mul_result():
    assert get_mul_result("(2,4)") == 8
    assert get_mul_result("[3,7]") == 0
    assert get_mul_result("(5,5)") == 25
    assert get_mul_result("(32,64]") == 0
    assert get_mul_result("(11,8)") == 88
    assert get_mul_result("(8,5)") == 40

def test_get_sum_mul():
    assert get_sum_mul(example_data) == 161
    assert get_sum_mul(data) == 179834255

def test_get_sum_mul_conditional():
    assert get_sum_mul_conditional(example_data2) == 48