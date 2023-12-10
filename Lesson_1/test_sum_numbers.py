from sum_numbers import sum_numbers


def test_add_number():
    assert sum_numbers(2,3) == 5

def test_add_number_negative():
    assert sum_numbers(2,2) == 5