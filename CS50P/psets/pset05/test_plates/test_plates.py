from plates import is_valid

def main():
    # “All vanity plates must start with at least two letters.”
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    # “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    # “No periods, spaces, or punctuation marks are allowed.”

    test_startWithTwoLetters()
    test_maximumMinimum()
    test_numbersMiddle()


def test_startWithTwoLetters():
    plates = ["C487", "A32", "10AA", "1BAA"]
    for plate in plates:
        assert is_valid(plate) == False


def test_maximumMinimum():
    plates = ["C", "B", "CS50AAA"]
    for plate in plates:
        assert is_valid(plate) == False


def test_numbersMiddle():
    plates = ["AA432A", "BA90C", "ZS12QQ"]
    for plate in plates:
        assert is_valid(plate) == False


def test_zero():
    plates = ["AA04", "BB09", "ZC00"]
    for plate in plates:
        assert is_valid(plate) == False


def test_punctuation():
    plates = ["_!AA15", "B?X__10", "-AB27", "A.B.C200"]
    for plate in plates:
        assert is_valid(plate) == False


def test_alphanuemric():
    plates = ["CS50$", "YORK#", "DC12@"]
    for plate in plates:
        assert is_valid(plate) == False 


if __name__ == "__main__":
    main()