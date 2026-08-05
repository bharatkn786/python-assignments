

# example 1:    Match and case example

num = int(input("Enter a number: "))

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")




# Example 2:    Exception example

age = int(input("Enter your age: "))

try:
    if age < 18:
        raise ExceptionGroup(
            "Validation Errors",
            [
                ValueError("Age must be 18 or above.")
            ]
        )

    print("You are eligible.")

except* ValueError as e:
    print("Exception:", e)




    