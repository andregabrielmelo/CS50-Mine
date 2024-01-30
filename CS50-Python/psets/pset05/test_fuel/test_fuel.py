from pytest import raises
from fuel import convert, gauge

def main():
    test_hasPercentageSign()
    test_hasSymbolSign()
    test_isInteger()
    test_value_error()
    test_zero_division()


def test_hasPercentageSign():
    fractions = ["1/4", "1/2", "3/4"]
    for fraction in fractions:
        assert "%" in gauge(convert(fraction))


def test_hasSymbolSign():
    fractions_full = ["99/100", "992/1000", "997/1000"]
    for fraction in fractions_full:
        assert gauge(convert(fraction)) == "F"
    
    fractions_empty = ["1/100", "9/1000", "7/1000"]
    for fraction in fractions_empty:
        assert gauge(convert(fraction)) == "E"


def test_isInteger():
    fractions = ["12/40", "23/60", "71/90"]
    for fraction in fractions:
        assert isinstance(convert(fraction), int)

def test_value_error():
    fractions = ["35/12", "98/34", "1000/10"]
    with raises(ValueError):
        for fraction in fractions:
            convert(fraction)


def test_zero_division():
    fractions = ["1/0", "0/0", "1000/0"]
    with raises(ZeroDivisionError):
        for fraction in fractions:
            convert(fraction)

if __name__ == "__main__":
    main()  