import random

def guess_the_number():
  secret_number = random.randint(1, 100)
  guess = 0
  while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < secret_number:
      print("Too low!")
    elif guess > secret_number:
      print("Too high!")
  print(f"Congratulations! You guessed the number {secret_number}.")

guess_the_number()
