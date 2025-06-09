temperature = int(input("Enter temperature"))
if temperature < 0 :
    print("It's freezing!")

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd")

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")

number = int(input("Enter a number: "))
if number >= 0:
    if number == 0:
        print(f"The number is zero.")
    else:
        print(f"{number} is positive.")
else:
    print(f"{number} id negative .")
