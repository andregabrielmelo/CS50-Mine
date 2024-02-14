import validators

def main():
    print(validate_mail(input("What's your e-mail: ")))


def validate_mail(mail):
    if validators.email(mail):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()