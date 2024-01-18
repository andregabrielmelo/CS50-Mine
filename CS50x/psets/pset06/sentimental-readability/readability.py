# TODO
import math


def main():
    text = input("Text: ")  # Get text from the user

    # Count letters, words and sentences in the text
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Grade the text using the Coleman-Liau index readability text
    grade = round(
        0.0588 * (letters / words * 100) - 0.296 * (sentences / words * 100) - 15.8
    )

    # Print the grade the person is in
    if grade < 1:
        print("Before Grade 1")
    elif grade > 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


def count_letters(text):
    count = 0
    for i in range(len(text)):
        if text[i].isalpha():
            count += 1

    return count


def count_words(text):
    count = 1  # Begins at one because the last word won't have a space after it
    for i in range(len(text)):
        if text[i] == " ":
            count += 1

    return count


def count_sentences(text):
    count = 0
    for i in range(len(text)):
        if text[i] == "." or text[i] == "!" or text[i] == "?":
            count += 1

    return count


if __name__ == "__main__":
    main()
