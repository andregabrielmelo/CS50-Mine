from numb3rs import validate

def main():
    test_numbers_in_range()
    # test_no_leading_zeros()


def test_numbers_in_range():
    assert validate("-1.-1.-1.-1") == False
    assert validate("0.0.0.0") == True 
    assert validate("255.255.255.255") == True
    assert validate("256.256.256.256") == False


def test_only_first_byte():
    assert validate("75.400.23.45") == False

# def test_no_leading_zeros():
#     assert validate("01.01.01.01") == False 
#     assert validate("001.001.001.001") == False

if __name__ == "__main__":
    main()