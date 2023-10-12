def main():
  """Prompts the user to input two numbers and an operation choice, performs the calculation, and displays the result."""

  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  op = input("Enter the operation (+, -, *, or /): ")

  if not isinstance(num1, (float, int)) or not isinstance(num2, (float, int)):
    print("Invalid input. Please enter two valid numbers.")
    return

  if op not in ["+", "-", "*", "/"]:
    print("Invalid operation. Please enter a valid operation (+, -, *, or /).")
    return

  result = None
  if op == "+":
    result = num1 + num2
  elif op == "-":
    result = num1 - num2
  elif op == "*":
    result = num1 * num2
  elif op == "/":
    result = num1 / num2

  print(f"{num1} {op} {num2} = {result}")


if __name__ == "__main__":
  main()
