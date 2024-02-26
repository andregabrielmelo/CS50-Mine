from bank import value

def main():
    test_zero()
    test_twenty()
    test_hundred()


def test_zero():
    words = ["HELLO", "hello", "HeLlo"]
    for word in words:
        assert value(word) == 0


def test_twenty():
    words = ["help", "hamburguer", "Helicopter"]
    for word in words:
        assert value(word) == 20

def test_hundred():
    words = ["the", "yah", "dash"]
    for word in words:
        assert value(word) == 100


if __name__ == "__main__":
    main()