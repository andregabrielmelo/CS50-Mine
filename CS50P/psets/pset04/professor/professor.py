import random


def main():
    # Get level 
    level = get_level()

    # Make problems based in the level 
    problems = generate_integer(level)

    # Prompt questions to the user 
    score = 0
    for i in range(len(problems)): # For each problem

        # Get the problems numbers, (x + y = )
        x, y = map(int, problems[i].split(" + "))

        times_wrong = 0
        while True:
            # Try getting the answer 
            try:
                # If the answer is wrong 3 times 
                if times_wrong == 3:
                    print(f"{x} + {y} = {x + y}")
                    break

                # Get user answer 
                answer = input(f"{problems[i]} = ")

                # If the user answer is wrong
                if int(answer) != x + y:
                    print("EEE")
                    raise ValueError

            # Invalid input or wrong answer
            except ValueError:
                times_wrong += 1
                pass
            # User got the answer right 
            else:
                score += 1
                break

    # User score
    print(f"Score: {score}")


def get_level():
    # Get the level
    while True:
        # try getting the level (1, 2 or 3)
        try:
            # Get level
            level = int(input("Level: "))

            # Verify if the level is valid (1, 2 or 3)
            if level not in range(1, 4):
                raise ValueError
        
        # If the input is invalid or not between what is expected
        except ValueError:
            pass
        else:
            # Return level as an integer
            return level


def generate_integer(level):

    # Dict for problems 
    problems = {}

    # Range of numbers in the problem (a to b)
    a = 0 if level == 1 else 10 ** (level - 1)
    b = (10 ** level) - 1

    # Make 10 problems 
    for i in range(10):

        # Create problem
        x = random.randint(a, b)
        y = random.randint(a, b)
        problems[i] = f"{x} + {y}"
    
    return problems


if __name__ == "__main__":
    main()