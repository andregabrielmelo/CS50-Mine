from twttr import shorten


def main():
    test_word()


def test_phrase():
    phrases = {
        "My twitter": "My twttr",
        "This big hamburguer": "Ths bg hmbrgr",
        "Love this pepperoni pizza": "Lv ths ppprn pzz",
    }

    for key in phrases:
        assert shorten(key) == phrases[key]


def test_word():
    words = {
        "twitter": "twttr",
        "hamburguer": "hmbrgr",
        "pizza": "pzz",
        "Ebay": "by",  # capital replacement
        "101 artic": "101 rtc",  # ommit numbers
        "Bro.": "Br.",  # omit punctuation
        "Hello_bye": "Hll_by",
    }

    for key in words:
        assert shorten(key) == words[key]


if __name__ == "__main__":
    main()
