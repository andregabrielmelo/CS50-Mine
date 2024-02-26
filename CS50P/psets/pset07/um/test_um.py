from um import count

def main():
    test_match_um_in_words()
    test_need_whitespaces_around_um()


def test_match_um_in_words():
    assert count("Kabum") == 0
    assert count("Jump") == 0
    assert count("human") == 0

def test_need_whitespaces_around_um():
    assert count("um, and,um, bye") == 2
    assert count("can you,um, jump") == 1

def test_case_insensitive():
    assert count("UM, can you, Um, pass me that") == 2
    assert count("I am, UM, new here") == 1


if __name__ == "__main__":
    main()