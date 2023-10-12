import random

def generate_password(length=12):
  """Generates a random password of the specified length."""

  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

  password = ""
  for i in range(length):
    password += random.choice(characters)

  return password

def main():
  """Prompts the user to specify the desired length of the password, generates a password of the specified length, and displays the generated password on the screen."""

  length = int(input("Enter the desired length of the password: "))

  password = generate_password(length)

  print(f"Your generated password is: {password}")


if __name__ == "__main__":
  main()
