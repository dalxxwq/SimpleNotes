try:
    num1 = float(input("Please enter ur first number: "))
    num2 = float(input("Please enter ur second number: "))

    final_answer = num1 / num2
    print(f"Ur answer is {final_answer}")

except ZeroDivisionError:
    print("Error: zero division is impossible")
except ValueError:
    print("Error: please enter valid numbers")
