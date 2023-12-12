from mean import *

def test_mean_with_ints():
    num_list = [1, 2, 3, 4, 5]
    observed_value = mean(num_list)
    expected_value = 3
    assert observed_value == expected_value

def test_mean_with_zero():
    num_list=[0, 2, 4, 6]
    observed_value = mean(num_list)
    expected_value = 3
    assert observed_value == expected_value

def test_mean_with_double():
    # This one will fail in Python 2
    num_list=[1, 2, 3, 4]
    observed_value = mean(num_list)
    expected_value = 2.5
    assert observed_value == expected_value

def test_mean_with_long():
    big = 100000000
    observed_value = mean(range(1,big))
    expected_value = big/2.0
    assert observed_value == expected_value

def test_mean_with_complex():
    # given that complex numbers are an unordered field
    # the arithmetic mean of complex numbers is meaningless
    num_list = [2 + 3j, 3 + 4j, -32 - 2j]
    observed_value = mean(num_list)
    expected_value = NotImplemented
    assert observed_value == expected_value
